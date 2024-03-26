## YOLOv8n-pose

The code has been successfully tested on both Ubuntu 22.04 and Windows 10 operating systems.


```bash
final/
├── preprocess/
    ├── channel_shift_demo.py
    └── channel_shift_aug.py
├── requirements.txt
├── environment.yml
├── best.pt
├── best.tflite
├── run_model_pt.py
├── run_model_tflite.py
├── convert2tflite.py
└── techreport.pdf
```


<details><summary>1. Create Conda Environments</summary>

- for pip users

```bash
$ conda env remove -n yuhs1
$ conda create -n yuhs1 python=3.10 -y
$ conda activate yuhs1
$ pip install ultralytics
$ pip install nvidia-pyindex
$ pip install onnx-graphsurgeon
$ pip install -r requirements.txt
```

- for Conda users

```bash
$ conda env create -f environment.yml
```

- for Docker users

```bash

```

</details>


<details><summary>2. Convert to .tflite</summary>

```bash
$ python convert2tflite.py
```

</details>


<details><summary>3. Execute run_model.py</summary>

```bash
# for best.pt inference
$ python run_model_pt.py ./imageList.txt test_data

# for best.tflite inference
$ python run_model_tflite.py ./imageList.txt test_data
```

</details>



<details><summary>4. Data augmentation</summary>

```bash
# ivslab_facial _testing_example_private_final
$ python predict.py

# preprocess
$ fitTest_aug.py
$ channel_shift_aug.py
```

</details>


<details><summary>5. Re-train</summary>

```bash
$ git clone https://github.com/ultralytics/ultralytics.git
```

</details>


- [Export Formats](https://docs.ultralytics.com/modes/export/#export-formats)
- [Usage](https://docs.ultralytics.com/integrations/tflite/#usage)
- [Model optimization](https://www.tensorflow.org/lite/performance/model_optimization)
- [Confusion about different TFLite quantization methods and corresponding output files #3153](https://github.com/ultralytics/ultralytics/issues/3153)
- [Improve TFLite INT8 detection accuracy #7372](https://github.com/ultralytics/ultralytics/pull/7372)
- [Interpreting YOLOv8 Pose outputs in tflite #4771](https://github.com/ultralytics/ultralytics/issues/4771)
    - [yolov8 tflite dg_export.ipynb](https://colab.research.google.com/drive/1yjCEwwFuMKvFJceSDfyWrUWOSfvLlPjl?usp=sharing#scrollTo=v_QB06rnjz9e)
        - [ultralytics_yolov8](https://github.com/DeGirum/ultralytics_yolov8)
- [Model optimization #6242](https://github.com/ultralytics/ultralytics/issues/6242)
- [ultralytics.utils.torch_utils.strip_optimizer(f='best.pt', s='')](https://docs.ultralytics.com/reference/utils/torch_utils/#ultralytics.utils.torch_utils.strip_optimizer)
- [How to prune YoloV8 model and save it for finetuning ? #3507](https://github.com/ultralytics/ultralytics/issues/3507)
- https://blog.csdn.net/qq_33596242/article/details/133774348
- https://blog.csdn.net/qq_40672115/article/details/130155924
- https://docs.ultralytics.com/zh/integrations/neural-magic/#benefits-of-integrating-neural-magics-deepsparse-with-yolov8
