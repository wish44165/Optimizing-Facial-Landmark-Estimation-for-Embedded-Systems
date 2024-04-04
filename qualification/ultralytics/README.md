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
├── facial_v4.yaml
├── facial_v4_x8.yaml
├── train.py
├── valid.py
├── predict.py
└── submit.py
```

</details>


<details><summary>Train</summary>

```
$ python train.py --model_name <model name> \
                  --yaml_path <yaml path> \
                  --n_epoch <training epochs> \
                  --n_patience <early stop> \
                  --bs <batch size> \
                  --imgsz <image size> \
                  --pose <pose weight> \
                  --n_worker <number of workers> \
                  --save_path <save path>

# e.g.
$ python train.py --model_name yolov8n-pose.pt --yaml_path facial.yaml --n_epoch 300 --n_patience 100 --bs 8 --imgsz 640 --n_worker $(nproc) --save_path ./runs/facial

# After iAutolabeling
$ python train.py
# output: ultralytics/runs/facial/train/weights/best.pt

# x8
# $ python train.py --model_name ./runs/facial/train/weights/best.pt --yaml_path facial_v4_x8.yaml --n_worker $(nproc) --save_path ./runs/facial
# output: ultralytics/runs/facial/train2/weights/best.pt
```

</details>


<details><summary>Valid</summary>

```
$ python valid.py --weight <trained model> \
                  --save_path <save path>
```

</details>


<details><summary>Predict</summary>

```
$ python predict.py --weight <trained model> \
                    --save_path <save path> \
                    --predict_folder <predict folder>
```

</details>


<details><summary>Submit</summary>

```
$ python submit.py
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

