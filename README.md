# Low-power Efficient and Accurate Facial-Landmark Detection for Embedded Systems

2024 IEEE International Conference on Multimedia and Expo

- [Low-power Efficient and Accurate Facial-Landmark Detection for Embedded Systems](https://aidea-web.tw/topic/b048c9a3-c3bc-4650-9674-f14f4c850f12)
- https://2024.ieeeicme.org/grand-challenge-proposals/

## Progress

- [ ] Stretch augmentation
- [ ] Channel shift
- [x] 06/03/2024 - Data augmentation (aug.py)
- [x] 06/03/2024 - Adjust single_cls, pose, degrees, shear, mosaic, mixup, copy_paste, erasing while training
- [x] 27/02/2024 - Iterative auto label (iAutolabeling/)
- [x] 22/02/2024 - Filter and split dataset (duplicateCheck.py, splitdata_v2.py)
- [x] 19/02/2024 - Split semi label (splitdata_yolo.py)
- [x] 17/02/2024 - Auto label approx. bbox (pts2yolo_v2.py) 
- [x] 16/02/2024 - YOLOv8-pose Setup (ultralytics/)
- [x] 15/02/2024 - Auto label with whole image (pts2yolo.py)
- [x] 14/02/2024 - Split dataset (splitdata.py)

---


## 1. Environmental Setup

<details>

<summary>Hardware Information</summary>

- CPU: AMD Ryzen 5 5600X 6-Core @ 12x 3.7GHz
- GPU: NVIDIA GeForce RTX 3060 Ti (8G)
- RAM: 48087MiB
  
</details>


<details><summary>Create Conda Environment</summary>

```
$ conda create -n yolov8 python=3.10 -y
$ conda activate yolov8
$ git clone https://github.com/ultralytics/ultralytics.git
$ cd ultralytics/
$ pip install ultralytics
$ pip install pyarrow
$ pip install scikit-learn
```

</details>




## 2. Reproducing Details


<details><summary>Datasets Download Links</summary>

### Stage 1 dataset

- [Download_Link.txt](https://www.aicreda.com/download/iVSFacialDataset)
- [ICME2024_Download_Link.txt](https://bit.ly/42q4XXU)

### Stage 2 dataset

- [ivslab_facial_test_private_qualification.zip.001](https://aidea-web.tw/file/b048c9a3-c3bc-4650-9674-f14f4c850f12-1706842899_train_test_dataset_2___ivslab_facial_test_private_qualification.zip.001)
- [ivslab_facial_test_private_qualification.zip.002](https://aidea-web.tw/file/b048c9a3-c3bc-4650-9674-f14f4c850f12-1706842899_train_test_dataset_2___ivslab_facial_test_private_qualification.zip.002)

```bash
$ cat ivslab_facial_test_private_qualification.zip.001 ivslab_facial_test_private_qualification.zip.002 > ivslab_facial_test_private_qualification.zip
$ unzip ivslab_facial_test_private_qualification.zip
```

</details>


<details><summary>Folder Structure on Local Machine</summary>

- Create the following folder structure on the local machine

    ```bash
    # Qualification Competition
    qualification/
    ├── preprocess/
        ├── visualCheck.py
        ├── visualCheck_filtered.py
        ├── splitdata.py
        ├── splitdata_v2.py
        ├── splitdata_yolo.py
        ├── duplicateCheck.py
        ├── pts2yolo.py
        ├── pts2yolo_v2.py
        └── aug.py
    preprocess/
    └── ultralytics/
        ├── facial.yaml
        ├── train.py
        ├── valid.py
        └── predict.py

    # Final Competition
    #mx/
    #├── requirements.txt
    #├── calculate.py
    #├── cal_model_size.py
    #├── cal_model_complexity.py
    #├── run_detection_pt.py
    #├── run_detection_onnx.py
    #├── best.csv
    #└── best.txt
    ```

</details>


<details><summary>Qualification Competition</summary>

```bash
# iAutolabeling_conf_0.2
$ for i in `seq 0 3`; do python main.py --curr_iter ${i} | tee iterLog${i}.txt; done
$ for i in `seq 4 19`; do python main.py --curr_iter ${i} --bs 32 | tee iterLog${i}.txt; done

# iAutolabeling_conf_0.3
$ for i in `seq 0 4`; do python main.py --curr_iter ${i} | tee iterLog${i}.txt; done
$ for i in `seq 5 19`; do python main.py --curr_iter ${i} --bs 32 | tee iterLog${i}.txt; done

# iAutolabeling_conf_0.5
$ for i in `seq 0 9`; do python main.py --curr_iter ${i} | tee iterLog${i}.txt; done
$ for i in `seq 10 19`; do python main.py --curr_iter ${i} | tee iterLog${i}.txt; done

# After iAutolabeling (v4, Adjust single_cls, pose, degrees, shear, mosaic, mixup, copy_paste, erasing while training)
$ python train.py
# output: ultralytics/runs/facial/train/weights/best.pt

# v4_x8
$ python train.py --model_name ./runs/facial/train/weights/best.pt --yaml_path facial_v4_x8.yaml --n_worker $(nproc) --save_path ./runs/facial
# output: ultralytics/runs/facial/train2/weights/best.pt

# submit
$ python predict.py
$ python submit.py
```

</details>


<details><summary>Final Competition</summary>



</details>




## 3. Demonstration




## 4. Leaderboard Scores




## 5. GitHub Acknowledgement




## 6. References

### Papers With Code

- [SPIGA: Shape Preserving Facial Landmarks with Graph Attention Networks](https://arxiv.org/pdf/2210.07233.pdf) ([GitHub](https://github.com/andresprados/spiga)) (2022)
- [Deep High-Resolution Representation Learning for Visual Recognition](https://arxiv.org/pdf/1908.07919.pdf) ([GitHub](https://github.com/HRNet/HRNet-Facial-Landmark-Detection)) (2019)
- [Deep Adaptive Attention for Joint Facial Action Unit Detection and Face Alignment](https://openaccess.thecvf.com/content_ECCV_2018/papers/Zhiwen_Shao_Deep_Adaptive_Attention_ECCV_2018_paper.pdf) ([GitHub](https://github.com/ZhiwenShao/JAANet)) (2018)
- [Facial Landmark Detection on 300W](https://paperswithcode.com/sota/facial-landmark-detection-on-300w)

### GitHub Repository

- [X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling)
- [Face-alignment-mobilenet-v2](https://github.com/WallZFE/Face-alignment-mobilenet-v2)
- [26M Flops Facial Landmark Detection](https://github.com/ainrichman/Peppa-Facial-Landmark-PyTorch)
- [yolov8-face-landmarks-opencv-dnn](https://github.com/hpc203/yolov8-face-landmarks-opencv-dnn)
- [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace)
- [FacialLandmark_Caffe](https://github.com/BobLiu20/FacialLandmark_Caffe)
- [FacialLandmarkDetection](https://github.com/nicknochnack/FacialLandmarkDetection)
- [Colour Shift](https://github.com/mayasarena/colour-shift)




## Citation
