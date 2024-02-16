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
src/
├── preprocess/
    └── data/
        ├── images/
            ├── train/
            └── val/
        └── labels/
            ├── train/
            └── val/
└── ultralytics/
    ├── facial.yaml
    ├── train.py
    └── valid.py
```

</details>


<details><summary>Train</summary>

```
$ python train.py --model_name <model name> \
                  --yaml_path <yaml path> \
                  --n_epoch <training epochs> \
                  --bs <batch size> \
                  --imgsz <image size> \
                  --n_worker <number of workers> \
                  --save_path <save path>
```

</details>


<details><summary>Valid</summary>

```
$ python valid.py --weight <trained model> \
                  --save_path <save path>
```

</details>


<details><summary>Reference</summary>

- [Model Training with Ultralytics YOLO](https://docs.ultralytics.com/modes/train/)
- [Pose Estimation](https://docs.ultralytics.com/tasks/pose/)
- [Pose Estimation on Custom Data using Ultralytics YOLOv8](https://ultralytics.medium.com/pose-estimation-on-custom-data-using-ultralytics-yolov8-ef63e103daea)
- [Train Yolov8 object detection on a custom dataset | Step by step guide | Computer vision tutorial](https://youtu.be/m9fH9OWn8YM?si=Npjpa4mdlA0vtYce)
- [Yolov8 with key points detection without object detection](https://github.com/ultralytics/ultralytics/issues/2929)
- [Yolov8 with key points detection without object detection](https://ai.stackexchange.com/questions/40664/yolov8-with-key-points-detection-without-object-detection)

</details>
