# Mosaic Program
Mosaic program은 YOLOv7 기반으로 작성되었으며, 현재 **얼굴**과 **사람** 인식이 가능하며, **번호판** 인식은 추가 예정.





## Setting Up Execution Environment

### Python Packages

#### Window >= 10

Required Python packages that can be installed using `pip`:

- **Python** >= 3.9
- **PySide** >= 6
- **pandas** >= 1.5.3
- **opencv-python** >= 4.7
- **numpy** >= 1.24
- **PyYAML** >= 6
- **qimage2ndarray** >= 1.10
- **scipy** >= 1.10
- **seaborn** >= 0.12

PyTorch는 CUDA를 먼저 설치 후, 해당 버전에 맞는 Torch를 설치할 것.

```
Example - CUDA 11.7 with PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```



## Model

[`face_person.pt`](https://github.com/Oh-JongJin/mosaic_program/releases/download/model/face_person.pt)



## Execution

```
python detect_ui.py
```

