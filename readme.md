#1.Install
##1.1.Requirements
- Linux (Windows is not officially supported)   
- Python 3.5+   
- PyTorch 1.1 or higher   
- CUDA 9.0 or higher   
- NCCL 2   
- GCC 4.9 or higher    
- mmcv   

##1.2.Install mmdetection
- a. Create a conda virtual environment and activate it.
~~~
   conda create -n open-mmlab python=3.7 -y   
   conda activate open-mmlab
~~~
- b. Install PyTorch and torchvision following the official instructions, e.g.,
~~~
   conda install pytorch torchvision -c pytorch
~~~
- c. Install build requirements and then install mmdetection. (We install pycocotools via the github repo instead of pypi because the pypi version is old and not compatible with the latest numpy.)
~~~
   pip install -r requirements/build.txt
   pip install "git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI"
   pip install -v -e .  # or "python setup.py develop"
~~~

#2.Train
   All of code we used are in the file /sumbit/code/mmdetection, and if you want to trian the model:   
      1.Choose a config file in the directory /sumbit/code/mmdetection/winebottle/winebottle_config/   
      2.You should note that **we used two models to train cap dataset and bottle dataset respectively**   
      3.The bottle config we used is **.\cascade_rcnn_r50_dconv_bottleall2_expand_ms.py**, the cap config we used is    
      **./cascade_rcnn_r50_dconv_capall2_expand_color_crop_rcnnH456.py**    
      4.find trian.py in the ./mmdetection/tools/, and prepare the CONFIG_FILE,  run the command in terminal:    
      ~~~
          python tools/train.py ${CONFIG_FILE}
      ~~~   
      5.waiting...   
      
#3.Inference
   The inference is simple too, you just need to run the inference_final.py in the ./mmdetection/winebottle/tools/, 
   but you should note:   
        1.Change the CONFIG_FILE path in the line 88-89   
        2.Change the MODEL_FILE path in the line 91-92   
        3.Set the GPU id in the line 94   
        4.Set image path file in line 174-174, all image absolute path are constitute a list and put in the json file,
           and I put the file used in the ./mmdetection/winebottle/, but you can't use it directly   
        5.The path in the 181-183 are not important, but insure are directory path in you computer   
        6.Finally, you need to choose a file path to get the inference result in line 185   
        7.Click run and wait(about 30 minutes)   
        
#4.Code Destription
   As I mentioned, all of code we use are in the file /submit/code/, and mmdetection toolbox give us a lot of help, 
   the main code of build model are based it, in the process of debugging, we change the code in the ./mmdetection/mmdet,
   about model struct and data augmentation.     
   A lot of helper scripts we write are in the ./mmdetection/winebottle/tools/       
   Config file we used are in the ./mmdetection/winebottle/tools/winebottle_config/ and ./mmdetection/configs/   
   
#5.Algorithm Destription
   - Backbone: ResNet50 + FPN
   - RCNN: Cascade-RCNN
   - Loss Function: CrossEntropy Loss
   - Sampler: RandomSampler
   - DCN: case the defects are in various shapes, we use DCN in the stage 2-4 of ResNet50 to get more characteristic
   - More anchors size of cap: case 7 defects in caps, we set 9 anchor ratios
   - SWA: fuse 3 model together, they are epoch 18, 19, 20, and weights are 0.09, 0.21, 0.7 respectively
   - Data Augmentation in train: Flip, Min iou Crop, Expand, Photo Metric Distortion, Resize
   - Data Augmentation in test: Flip, Multi scale, and crop for bottle dateset
        