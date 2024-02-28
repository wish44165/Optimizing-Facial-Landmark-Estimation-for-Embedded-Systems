## preprocess


<details><summary>1. Visualization</summary>

```bash
$ python visualCheck.py
```

</details>


<details><summary>2. Create Datasets</summary>

### v1 

- whole image as bounding box

```bash
$ python splitdata.py
```

- output: ../../datasets/data_v1/ (.pts)

```bash
$ python pts2yolo.py 
```

- output: ../../datasets/data_v1/labels/ (.txt)


### v2

```bash

```

</details>




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


<details><summary>Filtered Data Folder Structure</summary>

```
ivslab_facial_train_filtered/
├── 300W/
    ├── images/
    └── labels/
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
├── visualCheck_filtered.py
├── splitdata.py
├── splitdata_v2.py
├── splitdata_yolo.py
├── duplicateCheck.py
├── pts2yolo.py
└── pts2yolo_v2.py
```

</details>


<details><summary>Steps</summary>

0. visualCheck.py

- data: 3549 / 888 (v1-v3)
- data_filtered: 3249 / 813 (v4)

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

train conf: 0.5
nms: 0.3

</details>



