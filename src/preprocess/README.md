## preprocess


<details><summary>Original Data Folder Structure</summary>

```
ivslab_facial_train/
├── 300W/
    ├── images/
        └── .png
    └── labels/
        └── .pts
├── afw/
    ├── images/
    └── labels/
├── helen/
    ├── images/
    └── labels/
├── ibug/
    ├── images/
    └── labels/
└── IFPW/
    ├── images/
    └── labels/
```

</details>

---

<details><summary>Install Packages</summary>

```
$ pip install pyarrow
$ pip install scikit-learn
```

</details>


<details><summary>Folder Structure</summary>

```
preprocess/
├── visualCheck.py
├── splitdata.py
└── pts2yolo.py
```

</details>


<details><summary>Steps</summary>

0. visualCheck.py

### v1

1. splitdata.py
2. pts2yolo.py (whole image as bounding box)

### v2

1. splitdata.py
2. pts2yolo_v2.py (+- 20 pixels)

### v3

1. splitdata_yolo.py

### v4

1. duplicateCheck.py
2. splitdata_v2.py

</details>
