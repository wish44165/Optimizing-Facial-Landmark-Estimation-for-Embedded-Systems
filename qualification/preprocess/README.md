## preprocess


<details><summary>Folder Structure</summary>

```
preprocess/
├── visualCheck.py
├── visualCheck_filtered.py
├── splitdata.py
├── splitdata_v2.py
├── splitdata_yolo.py
├── semi_labeling.py
├── txt2json.py
├── duplicateCheck.py
├── pts2yolo.py
└── pts2yolo_v2.py
```

</details>


<details><summary>1. Visualization</summary>

```bash
$ python visualCheck.py
```

</details>


<details><summary>2. Create Datasets</summary>

- data: 3549 / 888 (v1-v3)
- data_filtered: 3249 / 813 (v4)

### version 1 (whole image as bounding box)

```bash
$ python splitdata.py
```

- output: `../../datasets/data_v1/` (.pts)

```bash
$ python pts2yolo.py 
```

- output: `../../datasets/data_v1/labels/` (.txt)


### version 2 (approximate bounding box with +- 20 pixels)

```bash
$ python splitdata.py
```

- output: `../../datasets/data_v1/` (.pts)

```bash
$ python pts2yolo_v2.py 
```

- output: `../../datasets/data_v1/labels/` (.txt)


### version 3 (semi labeling)

```bash
$ python splitdata_yolo.py
```

- output: `../../datasets/data_v2/` (.txt)


### version 4 (based on version 3 ../../datasets/yolo_labels)

```bash
$ python duplicateCheck.py
```

- output: `../../datasets/ivslab_facial_train_filtered/`, `../../datasets/ivslab_facial_train_filtered_details/`
  
```bash
$ python splitdata_v2.py
```

- output: `../../datasets/v0/` (.txt)

</details>


<details><summary>Semi labeling for yolo_labels</summary>
  
- Train a baseline model

```bash
$ cd ../ultralytics
$ python train.py --model_name yolov8n-pose.pt --yaml_path facial.yaml --n_epoch 300 --n_patience 100 --bs 8 --imgsz 640 --n_worker $(nproc) --save_path ./run/facial
```

- Predict the training dataset.

```bash
$ python predict.py --weight ./runs/facial/train/weights/best.pt \
                    --save_path ./runs/facial \
                    --predict_folder ../../datasets/v0/images/train
```

- Labeling the training set semi-automatically

```bash
$ cd ../preprocess
$ python semi_labeling.py
```

### Fine-tuning labels through X-AnyLabeling

- Convert the files to JSON format
```bash
$ python txt2json.py
```

- Open with X-AnyLabeling


</details>
