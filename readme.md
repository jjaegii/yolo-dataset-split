# yolo 데이터셋 나누기

## 설정

split.py에서 데이터 경로와 output 경로를 설정해준다.
ratio를 통해 train:val 비율을 조절할 수 있다 ex) 80:20을 원하면 -> ratio=(0.8, 0.2)

merge.py에서 train 폴더 경로와 합친 파일을 저장할 새로운 train 폴더 경로, val 폴더 경로와 합친 파일을 저장할 새로운 val 폴더 경로를 설정해준다.

## 실행

```python
python3 split.py
python3 merge.py
```

