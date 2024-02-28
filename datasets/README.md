## datasets


<details><summary>Commands</summary>

```bash
$ mkdir ivslab_facial_train/
$ unzip ivslab_facial_train.zip -d ivslab_facial_train/
$ unzip yolo_labels.zip
```

</details>


<details><summary>Folder Structure</summary>

```bash
datasets/
    ├── ivslab_facial_train.zip
    ├── ivslab_facial_train/
        ├── 300W/
            ├── images/ (.png / .jpg)
            └── labels/ (.pts)
        ├── afw/
        ├── helen/
        ├── ibug/
        └── IFPW/
    ├── yolo_labels.zip
    ├── yolo_labels/
        ├── 300W_labels/
            └── .txt
        ├── afw_labels/
        ├── helen_labels/
        ├── ibug_labels/
        └── IFPW_labels/
    ├── data_v1/
    ├── data_v2/
    ├── ivslab_facial_train_filtered/
    ├── ivslab_facial_train_filtered_details/
    └── v0/
```

</details>
