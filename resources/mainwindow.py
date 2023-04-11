# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1152, 722)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.video_widget = QLabel(Dialog)
        self.video_widget.setObjectName(u"video_widget")
        self.video_widget.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_widget.sizePolicy().hasHeightForWidth())
        self.video_widget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        self.video_widget.setFont(font)
        self.video_widget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.video_widget.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.video_widget)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_play = QPushButton(Dialog)
        self.pushButton_play.setObjectName(u"pushButton_play")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_play.sizePolicy().hasHeightForWidth())
        self.pushButton_play.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_play.setFont(font1)

        self.horizontalLayout_7.addWidget(self.pushButton_play)

        self.horizontalSlider_video = QSlider(Dialog)
        self.horizontalSlider_video.setObjectName(u"horizontalSlider_video")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.horizontalSlider_video.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_video.setSizePolicy(sizePolicy2)
        self.horizontalSlider_video.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.horizontalSlider_video)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.pushButton_showmore = QPushButton(Dialog)
        self.pushButton_showmore.setObjectName(u"pushButton_showmore")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_showmore.sizePolicy().hasHeightForWidth())
        self.pushButton_showmore.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.pushButton_showmore)

        self.groupBox_setting = QGroupBox(Dialog)
        self.groupBox_setting.setObjectName(u"groupBox_setting")
        font2 = QFont()
        font2.setFamilies([u"Noto Sans KR Medium"])
        font2.setPointSize(10)
        self.groupBox_setting.setFont(font2)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_setting)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.example_label = QLabel(self.groupBox_setting)
        self.example_label.setObjectName(u"example_label")
        self.example_label.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.example_label.sizePolicy().hasHeightForWidth())
        self.example_label.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setPointSize(8)
        self.example_label.setFont(font3)

        self.verticalLayout.addWidget(self.example_label)

        self.example_img = QLabel(self.groupBox_setting)
        self.example_img.setObjectName(u"example_img")
        sizePolicy.setHeightForWidth(self.example_img.sizePolicy().hasHeightForWidth())
        self.example_img.setSizePolicy(sizePolicy)
        self.example_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.example_img)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_person = QCheckBox(self.groupBox_setting)
        self.checkBox_person.setObjectName(u"checkBox_person")
        font4 = QFont()
        font4.setFamilies([u"Noto Sans KR Medium"])
        font4.setPointSize(13)
        self.checkBox_person.setFont(font4)

        self.horizontalLayout_3.addWidget(self.checkBox_person)

        self.checkBox_face = QCheckBox(self.groupBox_setting)
        self.checkBox_face.setObjectName(u"checkBox_face")
        self.checkBox_face.setFont(font4)

        self.horizontalLayout_3.addWidget(self.checkBox_face)

        self.checkBox_license = QCheckBox(self.groupBox_setting)
        self.checkBox_license.setObjectName(u"checkBox_license")
        self.checkBox_license.setEnabled(False)
        self.checkBox_license.setFont(font4)

        self.horizontalLayout_3.addWidget(self.checkBox_license)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.groupBox_setting)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_mosaic = QCheckBox(self.groupBox_setting)
        self.checkBox_mosaic.setObjectName(u"checkBox_mosaic")
        self.checkBox_mosaic.setFont(font4)
        self.checkBox_mosaic.setChecked(False)

        self.horizontalLayout_4.addWidget(self.checkBox_mosaic)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.spinBox_mosaic = QSpinBox(self.groupBox_setting)
        self.spinBox_mosaic.setObjectName(u"spinBox_mosaic")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.spinBox_mosaic.sizePolicy().hasHeightForWidth())
        self.spinBox_mosaic.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.spinBox_mosaic)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalSlider_mosaic = QSlider(self.groupBox_setting)
        self.horizontalSlider_mosaic.setObjectName(u"horizontalSlider_mosaic")
        self.horizontalSlider_mosaic.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.horizontalSlider_mosaic.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_mosaic.setSizePolicy(sizePolicy3)
        self.horizontalSlider_mosaic.setMaximum(99)
        self.horizontalSlider_mosaic.setOrientation(Qt.Horizontal)
        self.horizontalSlider_mosaic.setInvertedAppearance(False)
        self.horizontalSlider_mosaic.setInvertedControls(False)

        self.verticalLayout.addWidget(self.horizontalSlider_mosaic)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_blur = QCheckBox(self.groupBox_setting)
        self.checkBox_blur.setObjectName(u"checkBox_blur")
        self.checkBox_blur.setFont(font4)

        self.horizontalLayout_6.addWidget(self.checkBox_blur)

        self.why_label = QLabel(self.groupBox_setting)
        self.why_label.setObjectName(u"why_label")
        sizePolicy4.setHeightForWidth(self.why_label.sizePolicy().hasHeightForWidth())
        self.why_label.setSizePolicy(sizePolicy4)
        self.why_label.setMaximumSize(QSize(20, 20))
        self.why_label.setPixmap(QPixmap(u"question_mark.png"))
        self.why_label.setScaledContents(True)
        self.why_label.setOpenExternalLinks(False)

        self.horizontalLayout_6.addWidget(self.why_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.spinBox_blur = QSpinBox(self.groupBox_setting)
        self.spinBox_blur.setObjectName(u"spinBox_blur")
        sizePolicy5.setHeightForWidth(self.spinBox_blur.sizePolicy().hasHeightForWidth())
        self.spinBox_blur.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.spinBox_blur)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalSlider_blur = QSlider(self.groupBox_setting)
        self.horizontalSlider_blur.setObjectName(u"horizontalSlider_blur")
        self.horizontalSlider_blur.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.horizontalSlider_blur.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_blur.setSizePolicy(sizePolicy3)
        self.horizontalSlider_blur.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_blur)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.groupBox_setting)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_fileopen = QPushButton(Dialog)
        self.pushButton_fileopen.setObjectName(u"pushButton_fileopen")
        self.pushButton_fileopen.setEnabled(True)
        self.pushButton_fileopen.setFont(font4)
        self.pushButton_fileopen.setAutoDefault(True)
        self.pushButton_fileopen.setFlat(False)

        self.horizontalLayout_8.addWidget(self.pushButton_fileopen)

        self.pushButton_folderopen = QPushButton(Dialog)
        self.pushButton_folderopen.setObjectName(u"pushButton_folderopen")
        self.pushButton_folderopen.setEnabled(True)
        self.pushButton_folderopen.setFont(font4)
        self.pushButton_folderopen.setAutoDefault(True)
        self.pushButton_folderopen.setFlat(False)

        self.horizontalLayout_8.addWidget(self.pushButton_folderopen)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)

        self.pushButton_start = QPushButton(Dialog)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setFont(font4)

        self.horizontalLayout_2.addWidget(self.pushButton_start)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.status_label = QLabel(Dialog)
        self.status_label.setObjectName(u"status_label")
        font5 = QFont()
        font5.setFamilies([u"Noto Sans KR Medium"])
        font5.setPointSize(11)
        self.status_label.setFont(font5)

        self.horizontalLayout_5.addWidget(self.status_label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.progressBar_current = QProgressBar(Dialog)
        self.progressBar_current.setObjectName(u"progressBar_current")
        sizePolicy2.setHeightForWidth(self.progressBar_current.sizePolicy().hasHeightForWidth())
        self.progressBar_current.setSizePolicy(sizePolicy2)
        self.progressBar_current.setMaximumSize(QSize(16777215, 12))
        self.progressBar_current.setFont(font2)
        self.progressBar_current.setValue(0)
        self.progressBar_current.setTextVisible(True)
        self.progressBar_current.setInvertedAppearance(False)

        self.verticalLayout_5.addWidget(self.progressBar_current)

        self.progressBar_total = QProgressBar(Dialog)
        self.progressBar_total.setObjectName(u"progressBar_total")
        self.progressBar_total.setFont(font2)
        self.progressBar_total.setValue(0)

        self.verticalLayout_5.addWidget(self.progressBar_total)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.status_label_2 = QLabel(Dialog)
        self.status_label_2.setObjectName(u"status_label_2")
        font6 = QFont()
        font6.setFamilies([u"Noto Sans KR Medium"])
        font6.setPointSize(9)
        font6.setBold(True)
        self.status_label_2.setFont(font6)

        self.horizontalLayout_5.addWidget(self.status_label_2)

        self.remain = QLabel(Dialog)
        self.remain.setObjectName(u"remain")
        font7 = QFont()
        font7.setFamilies([u"Noto Sans KR Medium"])
        font7.setPointSize(9)
        self.remain.setFont(font7)

        self.horizontalLayout_5.addWidget(self.remain)

        self.remain_time_2 = QLabel(Dialog)
        self.remain_time_2.setObjectName(u"remain_time_2")
        self.remain_time_2.setFont(font7)

        self.horizontalLayout_5.addWidget(self.remain_time_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.pushButton_close = QPushButton(Dialog)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy6)
        self.pushButton_close.setFont(font4)

        self.verticalLayout_2.addWidget(self.pushButton_close)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"SIJUNG", None))
        self.video_widget.setText("")
        self.pushButton_play.setText("")
        self.pushButton_showmore.setText("")
        self.groupBox_setting.setTitle(QCoreApplication.translate("Dialog", u"\uc124\uc815", None))
        self.example_label.setText(QCoreApplication.translate("Dialog", u"    \uc608\uc2dc \uc774\ubbf8\uc9c0", None))
        self.example_img.setText(QCoreApplication.translate("Dialog", u"\uc608\uc2dc \uc774\ubbf8\uc9c0", None))
        self.checkBox_person.setText(QCoreApplication.translate("Dialog", u"\uc0ac\ub78c", None))
        self.checkBox_face.setText(QCoreApplication.translate("Dialog", u"\uc5bc\uad74", None))
        self.checkBox_license.setText(QCoreApplication.translate("Dialog", u"\ubc88\ud638\ud310", None))
        self.checkBox_mosaic.setText(QCoreApplication.translate("Dialog", u"\ubaa8\uc790\uc774\ud06c", None))
#if QT_CONFIG(tooltip)
        self.checkBox_blur.setToolTip(QCoreApplication.translate("Dialog", u"\uc2dc\uac04\uc774 \ub2e4\uc18c \uc18c\uc694\ub420 \uc218 \uc788\uc74c.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_blur.setText(QCoreApplication.translate("Dialog", u"\ube14\ub7ec", None))
#if QT_CONFIG(tooltip)
        self.why_label.setToolTip(QCoreApplication.translate("Dialog", u"\uc2dc\uac04\uc774 \ub2e4\uc18c \uc18c\uc694\ub420 \uc218 \uc788\uc74c", None))
#endif // QT_CONFIG(tooltip)
        self.why_label.setText("")
        self.pushButton_fileopen.setText(QCoreApplication.translate("Dialog", u"  \ud30c\uc77c \uc120\ud0dd", None))
        self.pushButton_folderopen.setText(QCoreApplication.translate("Dialog", u"  \ud3f4\ub354 \uc120\ud0dd", None))
        self.pushButton_start.setText(QCoreApplication.translate("Dialog", u"\uc2dc\uc791", None))
        self.status_label.setText(QCoreApplication.translate("Dialog", u"\uc9c4\ud589\ub960: ", None))
        self.status_label_2.setText(QCoreApplication.translate("Dialog", u"\uc608\uc0c1 \uc18c\uc694 \uc2dc\uac04: ", None))
        self.remain.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.remain_time_2.setText(QCoreApplication.translate("Dialog", u" \ucd08", None))
        self.pushButton_close.setText(QCoreApplication.translate("Dialog", u"\uc885\ub8cc", None))
    # retranslateUi

