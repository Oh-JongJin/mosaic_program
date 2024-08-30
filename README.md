# Mosaic Program
The Mosaic program is based on YOLOv7 and currently capable of recognizing **faces** and **people**. **License plate** recognition is planned to be added in the future.

Would you like me to explain or elaborate on any part of this translation?



## Setting Up Execution Environment

### Python Packages

#### Window ≧ 10

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

