## YOLOv8n-pose

```bash
final/
├── requirements.txt
├── best.pt
├── best.tflite
├── run_model_pt.py
├── run_model_tflite.py
└── techreport.pdf
```


<details>

<summary>0.1. Create Conda Environments</summary>

```bash
$ conda create -n yolov8 python=3.10 -y
$ conda activate yolov8
$ git clone https://github.com/ultralytics/ultralytics.git
$ cd ultralytics/
$ pip install nvidia-pyindex
$ pip install onnx-graphsurgeon
$ pip install -r requirements.txt
```
  
</details>


<details><summary>0.2. Convert to .tflite</summary>

```bash
$ python convert2tflite.py
```

</details>


<details><summary>1.1. Execute run_model_pt.py</summary>

```bash
$ python run_model_pt.py ./imageList.txt test_data
```

</details>


<details><summary>1.2. Execute run_model_tflite.py</summary>

```bash
$ python run_model_tflite.py ./imageList.txt test_data
```

</details>



- [Export Formats](https://docs.ultralytics.com/modes/export/#export-formats)
- [Usage](https://docs.ultralytics.com/integrations/tflite/#usage)
