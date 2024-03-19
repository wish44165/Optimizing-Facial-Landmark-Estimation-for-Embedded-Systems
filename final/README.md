## YOLOv8n-pose

```bash
final/
├── requirements.txt
├── best.pt
├── run_model.py
└── techreport.pdf
```


<details>

<summary>1. Create Conda Environments</summary>

```bash
$ conda create -n yolov8 python=3.10 -y
$ conda activate yolov8
$ pip install ultralytics
$ git clone https://github.com/ultralytics/ultralytics.git
$ cd ultralytics/
```
  
</details>


<details><summary>2. Execute run_model.py</summary>

```bash
$ python run_model.py ./imageList.txt test_data
```

</details>
