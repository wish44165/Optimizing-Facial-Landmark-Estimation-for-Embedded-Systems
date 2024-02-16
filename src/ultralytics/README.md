## [Ultralytics](https://github.com/ultralytics/ultralytics)


<details><summary>Create Conda Environment</summary>

```
$ conda create -n yolov8 python=3.10 -y
$ conda activate yolov8
$ git clone https://github.com/ultralytics/ultralytics.git
$ cd ultralytics/
$ pip install ultralytics
```

</details>


<details><summary>Folder Structure</summary>

```
ultralytics/
├── facial.yaml
├── train_facial.py
├── predict_facial.py
└── data/
    ├── images/
        ├── train/
        └── val/
    └── labels/
        ├── train/
        └── val/
```

</details>


<details><summary>Train</summary>

```
$ python train_facial.py
```

</details>


<details><summary>Inference</summary>

```
$ python predict_facial.py
```

</details>


<details><summary>Reference</summary>

- [Model Training with Ultralytics YOLO](https://docs.ultralytics.com/modes/train/)
- [Pose Estimation on Custom Data using Ultralytics YOLOv8](https://ultralytics.medium.com/pose-estimation-on-custom-data-using-ultralytics-yolov8-ef63e103daea)
- [Train Yolov8 object detection on a custom dataset | Step by step guide | Computer vision tutorial](https://youtu.be/m9fH9OWn8YM?si=Npjpa4mdlA0vtYce)

</details>
