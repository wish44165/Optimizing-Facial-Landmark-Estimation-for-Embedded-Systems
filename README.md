## Optimizing Facial-Landmark Estimation for Embedded Systems through Iterative Autolabeling and Model Pruning


2024 IEEE International Conference on Multimedia and Expo


- [[2024 IEEE International Conference on Multimedia and Expo](https://2024.ieeeicme.org/)] [[IEEE ICME 2024 Grand Challenges](https://pairlabs.ai/ieee-icme-2024-grand-challenges/)]
- [[Qualification](https://aidea-web.tw/topic/b048c9a3-c3bc-4650-9674-f14f4c850f12)] [[Final](https://aidea-web.tw/topic/2e3e61b7-fbd0-417f-aba3-15124ba1b5cd?focus=intro)] [[ICME 2024 GC PAIR Competition Final Rankings](https://pairlabs.ai/icme-2024-gc-pair-competition-final-rankings/)]


The code has been successfully tested on both Ubuntu 22.04 and Windows 10 operating systems.




<details>

<summary>Progress</summary>

- [ ] 07/05/2024 - Camera-Ready Grand Challenge Paper submission
- [ ] 17/04/2024 - Grand Challenge  Paper Acceptance Notification
- [x] 10/04/2024 - Grand Challenge Paper Submission
- [x] 03/04/2024 - Imgsz=64, Conf, IOU, args.yaml, submission_v15.zip (v10_64_pruning/runs/facial/step_12_finetune/weights/)
- [x] 02/04/2024 - submission_v14.zip (c_step6/)
- [x] 01/04/2024 - Continue pruning, submission_v13.zip (v9_96_pruning/step_15_finetune/ -> v9_96_pruning_c/step_1_finetune/ -> c_step1/)
- [x] 31/03/2024 - C3TR, submission_v12.zip (v9_96_pruning/)
- [x] 30/03/2024 - DWConv, submission_v11.zip (v9_96/)
- [x] 29/03/2024 - submission_v10.zip (v8_128_pruning/)
- [x] 28/03/2024 - Model pruning (yolov8_pruning.py), submission_v9.zip (v8_96_pruning/)
- [x] 26/03/2024 - Channel shift augmentation (channel_shift_aug.py), submission_v8.zip (v8_160/)
- [x] 25/03/2024 - submission_v5.zip (best_v3.pt)
- [x] 24/03/2024 - submission_v4.zip (best_v2.pt)
- [x] 23/03/2024 - submission_v3.zip (best_v1.pt, 7.93)
- [x] 22/03/2024 - submission_v2.zip (best_v1.pt, 0.0: ImportError: cannot import name 'Self' from 'typing_extensions' (/home/ivslab/anaconda3/lib/python3.10/site-packages/typing_extensions.py))
- [x] 21/03/2024 - submission_v1.zip (best_v1.pt, 0.0: The requirements.txt file you uploaded is missing quite a few items, such as opencv, among others.)
- [x] 20/03/2024 - submission_v0.zip (best_v1.pt, 0.0: Lack tflite model file.)
- [x] 06/03/2024 - Data augmentation (copy_aug.py)
- [x] 06/03/2024 - Adjust single_cls, pose, degrees, shear, mosaic, mixup, copy_paste, erasing while training
- [x] 27/02/2024 - Iterative auto label (iAutolabeling/)
- [x] 22/02/2024 - Filter and split dataset (duplicateCheck.py, splitdata_v2.py)
- [x] 19/02/2024 - Split semi label (splitdata_yolo.py)
- [x] 17/02/2024 - Auto label approx. bbox (pts2yolo_v2.py) 
- [x] 16/02/2024 - YOLOv8-pose Setup (ultralytics/)
- [x] 15/02/2024 - Auto label with whole image (pts2yolo.py)
- [x] 14/02/2024 - Split dataset (splitdata.py)
  
</details>




## 1. Environmental Setup

<details>

<summary>Hardware Information</summary>

- CPU: AMD Ryzen 5 5600X 6-Core @ 12x 3.7GHz
- GPU: NVIDIA GeForce RTX 3060 Ti (8G)
- RAM: 48087MiB
  
</details>


<details><summary>Create Conda Environment</summary>

```bash
# Qualification competition
$ conda create -n yolov8 python=3.10 -y
$ conda activate yolov8
$ git clone https://github.com/ultralytics/ultralytics.git
$ cd ultralytics/
$ pip install ultralytics
$ pip install pyarrow
$ pip install scikit-learn

# Final competition
$ conda env remove -n yuhs1
$ conda create -n yuhs1 python=3.10 -y
$ conda activate yuhs1
$ pip install ultralytics
$ pip install nvidia-pyindex
$ pip install onnx-graphsurgeon
# https://github.com/wish44165/Optimizing-Facial-Landmark-Estimation-for-Embedded-Systems/blob/main/final/requirements.txt
$ pip install -r requirements.txt
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
    # Qualification competition
    qualification/
    ├── iAutolabeling/
    ├── preprocess/
        ├── visualCheck.py
        ├── visualCheck_filtered.py
        ├── splitdata.py
        ├── splitdata_v2.py
        ├── splitdata_yolo.py
        ├── semi_labeling.py
        ├── txt2json.py
        ├── duplicateCheck.py
        ├── pts2yolo.py
        ├── pts2yolo_v2.py
        ├── copy_aug.py
        └── fitTest_aug.py
    └── ultralytics/
        ├── facial.yaml
        ├── facial_v4.yaml
        ├── facial_v4_x8.yaml
        ├── train.py
        ├── valid.py
        ├── predict.py
        └── submit.py

    # Final competition
    final/
    ├── C3TR/
    ├── demo/
    ├── preprocess/
        ├── channel_shift_demo.py
        └── channel_shift_aug.py
    ├── pruning/
        ├── ultralytics/utils/loss.py
        └── yolov8_pruning.py
    ├── requirements.txt
    ├── environment.yml
    ├── writeImageList.py
    ├── best.pt
    ├── best.tflite
    ├── run_model_pt.py
    ├── run_model_tflite.py
    ├── convert2tflite.py
    └── techreport.pdf
    ```

</details>


<details><summary>Qualification Competition</summary>

- [preprocess](https://github.com/wish44165/Optimizing-Facial-Landmark-Estimation-for-Embedded-Systems/tree/main/qualification/preprocess)
- [iAutolabeling](https://github.com/wish44165/iAutolabeling)
- [ultralytics](https://github.com/wish44165/Optimizing-Facial-Landmark-Estimation-for-Embedded-Systems/tree/main/qualification/ultralytics)

</details>


<details><summary>Final Competition</summary>

- [pruning](https://github.com/wish44165/Optimizing-Facial-Landmark-Estimation-for-Embedded-Systems/tree/main/final)

</details>




## 3. Demonstration

### 3.1. Synergizing Data Annotations

<img src="https://github.com/wish44165/Optimizing-Facial-Landmark-Estimation-for-Embedded-Systems/blob/main/assets/103_synergized.png" alt="synergized" width="70%">

### 3.2. Iterative Autolabeling Enhancement

<img src="https://github.com/wish44165/Optimizing-Facial-Landmark-Estimation-for-Embedded-Systems/blob/main/assets/103_refined.png" alt="refined" width="70%" >

### 3.3. Channel Shift Augmentation

<img src="https://github.com/wish44165/Optimizing-Facial-Landmark-Estimation-for-Embedded-Systems/blob/main/assets/103_shifted.png" alt="shifted" width="70%" >




## 4. Leaderboard Scores

### 4.1. Qualification Competition

- [best.pt]()

| Leaderboards     | Filename               | Upload time         | Evaluation result | Ranking |
| ---------------- | ---------------------- | ------------------- | ----------------- | ------- |
| Public & Private | submission.zip         | 2024-03-10 01:48:13 | 18.808020         | 1/26    |


### 4.2. Final Competition

- [best.pt]() [best.tflite]()

| User  | Score | Accuracy (%) | Model Complexity (GFLOPs) | Model Size (MB) | Speed (ms) | Power (W) |
| ----- | ----- | ------------ | ------------------------- | --------------- | ---------- | --------- |
| yuhs1 | 7.78  | 19.30        | 0.08                      | 2.25            | 8.12       | 1.64      |




## 5. GitHub Acknowledgement

- [Official YOLOv8](https://github.com/ultralytics/ultralytics)
- [Torch Pruning](https://github.com/VainF/Torch-Pruning)
- [X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling)
- [Colour Shift](https://github.com/mayasarena/colour-shift)




## Citation
```

```
