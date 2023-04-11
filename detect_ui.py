# import argparse

import os
import sys
import time

import cv2
import time
import argparse
import datetime
import math

import qimage2ndarray
import torch
import torch.backends.cudnn as cudnn
import multiprocessing as mp
import numpy as np

from pathlib import Path
from PySide6.QtWidgets import QDialog, QFileDialog, QApplication, QMessageBox, QStyle
from PySide6.QtCore import Slot, Qt, QUrl, QByteArray
from PySide6.QtGui import QIcon, QPixmap, QImage, QMovie
from PySide6.QtMultimedia import QMediaFormat, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from multiprocessing import Process, Queue
from curve_thread import CurveThread

from clock import Clock
from consumer import Consumer
from resources.mainwindow import Ui_Dialog


def get_supported_mime_types():
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    return result


class Window(QDialog, Ui_Dialog):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        # Clock
        p = Process(name='Clock', target=Clock, args=(q_clock,), daemon=True)
        p.start()
        self.consumer = Consumer(q_clock)
        self.consumer.poped.connect(self.clock)
        #

        self.setGeometry(655, 140, 1152, 723)
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_close.setShortcut('Ctrl+W')

        self.pushButton_play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.pushButton_fileopen.setIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        self.pushButton_folderopen.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))
        self.pushButton_showmore.setIcon(self.style().standardIcon(QStyle.SP_ArrowBack))

        self.groupBox_setting.setVisible(False)
        self.pushButton_start.setEnabled(False)
        self.why_label.setPixmap(QPixmap('resources/question_mark.png'))
        self.init_size = self.size()

        self.setWindowIcon(QIcon('resources/logo.ico'))
        self.open_path = None
        self.save_path = None
        self.yolo_mp = None
        self.remain_time = None
        self._mime_types = []

        self.checkBox_person.stateChanged.connect(self.detect_person)
        self.checkBox_face.stateChanged.connect(self.detect_face)

        self.detect_type = ''
        self.print_type = ''
        self.value = 0
        self.frame = 0
        self.all_value = []

        self.file_count = 0
        self.flag = False
        self.pushButton_showmore.clicked.connect(self.see_more)
        self.pushButton_fileopen.clicked.connect(self.open_file)
        self.pushButton_folderopen.clicked.connect(self.open_folder)
        self.pushButton_start.clicked.connect(self.detect_start)

        self.horizontalSlider_mosaic.valueChanged.connect(self.mosaic_slider)
        self.spinBox_mosaic.valueChanged.connect(self.mosaic_spinbox)

        self.horizontalSlider_blur.valueChanged.connect(self.blur_slider)
        self.spinBox_blur.valueChanged.connect(self.blur_spinbox)

        self.complete_frame, self.total_frames, self.count_file, self.total_file = None, None, None, None

        # VideoWidget
        # self.mediaPlayer = QMediaPlayer()
        # self.videoWidget = QVideoWidget()
        # self.verticalLayout_video.addWidget(self.mediaPlayer)

    def check_all(self):
        if (self.checkBox_person.isChecked() or self.checkBox_face.isChecked()) and \
                (self.checkBox_mosaic.isChecked() or self.checkBox_blur.isChecked()):
            self.pushButton_start.setEnabled(True)
        else:
            self.pushButton_start.setEnabled(False)

    def mosaic_slider(self):
        self.checkBox_blur.setChecked(False)
        value = self.horizontalSlider_mosaic.value()
        self.spinBox_mosaic.setValue(value)

        if self.checkBox_mosaic.isChecked() and self.checkBox_person.isChecked():
            self.detect_type, self.print_type, self.value = 'person', 'mosaic', value
            self.exam_img_update('person', 'mosaic', value)
        elif self.checkBox_mosaic.isChecked() and self.checkBox_face.isChecked():
            self.detect_type, self.print_type, self.value = 'face', 'mosaic', value
            self.exam_img_update('face', 'mosaic', value)

        self.check_all()

    def mosaic_spinbox(self):
        self.horizontalSlider_mosaic.setValue(self.spinBox_mosaic.value())

    def blur_slider(self):
        self.checkBox_mosaic.setChecked(False)
        value = self.horizontalSlider_blur.value()
        self.spinBox_blur.setValue(value)

        if self.checkBox_blur.isChecked() and self.checkBox_person.isChecked():
            self.detect_type, self.print_type, self.value = 'person', 'blur', value
            self.exam_img_update('person', 'blur', value)
        elif self.checkBox_blur.isChecked() and self.checkBox_face.isChecked():
            self.detect_type, self.print_type, self.value = 'face', 'blur', value
            self.exam_img_update('face', 'blur', value)

        self.check_all()

    def exam_img_update(self, detect_type, print_type, value):
        if value == 0:
            file_path = 'resources/example/example.jpg'
        else:
            file_path = f'resources/example/result/{print_type}/{print_type}_{detect_type}_{value}.jpg'
        self.example_img.setPixmap(QPixmap(file_path).scaled(self.example_img.width(),
                                                             self.example_img.height(),
                                                             Qt.IgnoreAspectRatio))

    def detect_person(self):
        if self.checkBox_person.isChecked():
            if self.checkBox_face.isChecked():
                self.checkBox_face.setChecked(False)
        self.check_all()

    def detect_face(self):
        if self.checkBox_face.isChecked():
            if self.checkBox_person.isChecked():
                self.checkBox_person.setChecked(False)
        self.check_all()

    def blur_spinbox(self):
        self.horizontalSlider_blur.setValue(self.spinBox_blur.value())

    def see_more(self):
        if self.flag is False:
            self.groupBox_setting.setVisible(True)
            self.pushButton_showmore.setIcon(self.style().standardIcon(QStyle.SP_ArrowForward))
            self.flag = True
            self.example_img.setPixmap(QPixmap('resources/example/example.jpg').scaled(self.example_img.width(),
                                                                                       self.example_img.height(),
                                                                                       Qt.IgnoreAspectRatio))
        else:
            self.groupBox_setting.setVisible(False)
            self.pushButton_showmore.setIcon(self.style().standardIcon(QStyle.SP_ArrowBack))
            self.flag = False

    def detect_start(self):
        if self.detect_type == 'person':
            detect_type = '사람'
        elif self.detect_type == 'face':
            detect_type = '얼굴'
        else:
            detect_type = None

        if self.print_type == 'mosaic':
            print_type = '모자이크'
            self.all_value = [self.detect_type, self.print_type, self.value]
        elif self.print_type == 'blur':
            print_type = '블러'
            self.all_value = [self.detect_type, self.print_type, self.value * 2 - 1]
        else:
            print_type = None

        if not None in self.all_value:
            answer = QMessageBox.question(self, '확인', f'인식된 모든 {detect_type}을 {print_type} 처리 하시겠습니까!',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            print(self.all_value)
            if answer == QMessageBox.Yes:
                self.select()
                self.pushButton_start.setEnabled(False)

    def open_file(self):
        file_name = QFileDialog(self, '파일 선택')
        file_name.setFileMode(QFileDialog.FileMode.ExistingFiles)

        if file_name.exec():
            path = file_name.selectedFiles()
            if len(path) == 1:
                self.open_path = os.path.abspath(path[0])
                self.file_count = 1
            else:
                self.open_path = path
                self.file_count = 2

            # self.mediaPlayer.setVideoOutput(self.videoWidget)
            # url = file_dialog.selectedUrls()[0]
            # print(url)
            # self.mediaPlayer.setSource(url)
            # self.mediaPlayer.play()

    def open_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, '폴더 선택', '/')
        if len(folder_name) >= 1:
            self.open_path = folder_name
            self.file_count = 3

    def select(self):
        file_name = QFileDialog.getExistingDirectory(self, '저장 경로 선택')
        if file_name:
            self.save_path = file_name

            mp.freeze_support()

            _producer = detect
            p = Process(name='producer', target=_producer, args=(
                q, self.open_path, opt, self.save_path, self.all_value, self.file_count), daemon=True)
            self.yolo_mp = CurveThread(q)
            self.yolo_mp.poped.connect(self.pbar_update)
            self.yolo_mp.start()
            self.consumer.start()

            with torch.no_grad():
                p.start()

            loading = 'resources/loading.gif'
            self.loading = QMovie(loading, QByteArray(), self)
            self.loading.setCacheMode(QMovie.CacheAll)
            self.loading.setSpeed(100)
            self.video_widget.setMovie(self.loading)
            self.loading.start()

    @Slot(str)
    def pbar_update(self, data: list):
        if self.loading.state() == QMovie.MovieState.Running:
            self.loading.stop()

        # print(f'{self.count_file}/{self.total_file} {self.complete_frame}/{self.total_frames}')
        self.complete_frame, self.total_frames, self.count_file, self.total_file = data[0], data[1], data[2], data[3]
        self.progressBar_current.setValue((self.complete_frame / self.total_frames) * 100)
        self.progressBar_total.setValue((self.count_file + 1) / self.total_file * 100)
        self.remain_time = data[4] * (self.total_frames - self.complete_frame)
        # print(f'{self.count_file} + 1 / {self.total_file} * 100 = {(int(self.count_file) + 1 / self.total_file) * 100}')

        # current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # if int(current_time[-1]) % 1 == 0:
        #     remain_time = data[4] * (self.total_frames - self.complete_frame)
        #     self.remain_time.setText(f'{datetime.timedelta(seconds=math.ceil(remain_time))}')
        #     print(f'{self.count_file}/{self.total_file} {self.complete_frame}/{self.total_frames}')

        img = data[5]
        h, w, c = img.shape
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        self.video_widget.setPixmap(QPixmap.fromImage(qImg).scaled(self.video_widget.width(),
                                                                   self.video_widget.height(),
                                                                   Qt.IgnoreAspectRatio))

    @Slot()
    def clock(self, data):
        # current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(data)))
        if self.remain_time is not None:
            self.remain.setText(f'{datetime.timedelta(seconds=math.ceil(self.remain_time))}')

    def close(self):
        if self.consumer.isRunning():
            self.consumer.stop()
        if self.yolo_mp is not None and self.yolo_mp.isRunning():
            self.yolo_mp.stop()
        sys.exit()

    def closeEvent(self, e):
        if self.consumer.isRunning():
            self.consumer.stop()
        if self.yolo_mp.isRunning():
            self.yolo_mp.stop()


def detect(queue: Queue, source, option, save_file_path, what_checked, filecount=0):
    from models.experimental import attempt_load
    from utils.datasets import LoadStreams, LoadImages, LoadImagesOne_or_More
    from utils.general import check_img_size, check_imshow, non_max_suppression, scale_coords, set_logging
    from utils.plots import blur, blur_circle, mosaic
    from utils.torch_utils import select_device, TracedModel

    opt = option
    save_dir = Path(save_file_path)
    file_count = filecount
    weights, view_img, save_txt, imgsz, trace, source = 'face_person.pt', True, True, 640, not True, source
    # f'source: {source}, {type(source)}')
    if source is not None:
        save_img = True
        webcam = False

        # Initialize
        set_logging()
        device = select_device(opt.device)
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        model = attempt_load(weights, map_location=device)  # load FP32 model
        stride = int(model.stride.max())  # model stride
        imgsz = check_img_size(imgsz, s=stride)  # check img_size

        if trace:
            model = TracedModel(model, device, opt.img_size)

        if half:
            model.half()  # to FP16

        # Second-stage classifier 
        # classify = False
        # if classify:
        #     modelc = load_classifier(name='resnet101', n=2)  # initialize
        #     modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model']).to(device).eval()

        # Set Dataloader
        vid_path, vid_writer = None, None
        # if file_count == 3:
        #     dataset = LoadImages(source, img_size=imgsz, stride=stride)
        # elif file_count == 2:
        #     dataset = LoadImagesOne_or_More(source, img_size=imgsz, stride=stride)
        # elif file_count == 1:
        #     dataset = LoadImagesOne_or_More(source, img_size=imgsz, stride=stride)
        dataset = LoadImagesOne_or_More(source, img_size=imgsz, stride=stride, filecount=filecount)

        print(f'file count, source: {file_count, source}')

        # Get names and colors
        names = model.module.names if hasattr(model, 'module') else model.names
        # colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

        # Run inference
        if device.type != 'cpu':
            model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
        old_img_w = old_img_h = imgsz
        old_img_b = 1

        t0 = time.time()
        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Warmup
            if device.type != 'cpu' and (
                    old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
                old_img_b = img.shape[0]
                old_img_h = img.shape[2]
                old_img_w = img.shape[3]
                # for i in range(3):
                #     model(img, augment=opt.augment)[0]

            # Inference
            with torch.no_grad():  # Calculating gradients would cause a GPU memory leak
                pred = model(img, augment=opt.augment)[0]

            # Apply NMS
            pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes,
                                       agnostic=opt.agnostic_nms)

            # Apply Classifier
            # if classify:
            #     pred = apply_classifier(pred, modelc, img, im0s)

            start_time = time.time()
            # Process detections
            for i, det in enumerate(pred):  # detections per image
                if webcam:  # batch_size >= 1
                    p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
                else:
                    p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)

                p = Path(p)  # to Path

                save_path = str(save_dir / p.name)  # img.jpg
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        if save_img or view_img:  # Add bbox to image
                            label = f'{names[int(cls)]}'
                            if label == 'person' and label == what_checked[0]:
                                if what_checked[1] == 'mosaic':
                                    mosaic(xyxy, im0, label=label, strength=what_checked[2])
                                elif what_checked[1] == 'blur':
                                    blur(xyxy, im0, label=label, strength=what_checked[2])

                            elif label == 'face' and label == what_checked[0]:
                                if what_checked[1] == 'mosaic':
                                    mosaic(xyxy, im0, label=label, strength=what_checked[2])
                                elif what_checked[1] == 'blur':
                                    im0 = blur_circle(xyxy, im0, label=label, strength=what_checked[2])

                # Save results (image with detections)
                if save_img:
                    if dataset.mode == 'image':
                        cv2.imwrite(save_path, im0)
                        print(f" The image with the result is saved in: {save_path}")
                    else:  # 'video' or 'stream'
                        if vid_path != save_path:  # new video
                            vid_path = save_path
                            if isinstance(vid_writer, cv2.VideoWriter):
                                vid_writer.release()  # release previous video writer
                            if vid_cap:  # video
                                fps = vid_cap.get(cv2.CAP_PROP_FPS)
                                w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                                h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                            else:  # stream
                                fps, w, h = 30, im0.shape[1], im0.shape[0]
                                save_path += '.mp4'
                            vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                        vid_writer.write(im0)

            # if dataset.mode != 'image':
            end_time = time.time() - start_time
            data = [dataset.frame, dataset.nframes, dataset.count, dataset.nf, end_time, im0]
            queue.put(data)

        print(f'Done. ({time.time() - t0:.3f}s)')
        os.startfile(save_file_path)
        mp.freeze_support()


if __name__ == '__main__':
    mp.freeze_support()

    parser = argparse.ArgumentParser()
    parser.add_argument('--img-size', type=int, default=416, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--no-trace', action='store_true', help='don`t trace model')
    opt = parser.parse_args()

    q = Queue()
    q_clock = Queue()

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
