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



## 6. References


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
- [SPIGA: Shape Preserving Facial Landmarks with Graph Attention Networks](https://arxiv.org/pdf/2210.07233.pdf) ([GitHub](https://github.com/andresprados/spiga)) (2022)
- [Deep High-Resolution Representation Learning for Visual Recognition](https://arxiv.org/pdf/1908.07919.pdf) ([GitHub](https://github.com/HRNet/HRNet-Facial-Landmark-Detection)) (2019)
- [Deep Adaptive Attention for Joint Facial Action Unit Detection and Face Alignment](https://openaccess.thecvf.com/content_ECCV_2018/papers/Zhiwen_Shao_Deep_Adaptive_Attention_ECCV_2018_paper.pdf) ([GitHub](https://github.com/ZhiwenShao/JAANet)) (2018)
- [Facial Landmark Detection on 300W](https://paperswithcode.com/sota/facial-landmark-detection-on-300w)
- [Face-alignment-mobilenet-v2](https://github.com/WallZFE/Face-alignment-mobilenet-v2)
- [26M Flops Facial Landmark Detection](https://github.com/ainrichman/Peppa-Facial-Landmark-PyTorch)
- [yolov8-face-landmarks-opencv-dnn](https://github.com/hpc203/yolov8-face-landmarks-opencv-dnn)
- [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace)
- [FacialLandmark_Caffe](https://github.com/BobLiu20/FacialLandmark_Caffe)
- [FacialLandmarkDetection](https://github.com/nicknochnack/FacialLandmarkDetection)

</details>

