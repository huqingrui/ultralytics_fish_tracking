# Handling instructions (for beginners)

## How to use the tracking program
If you are tracking with data we have trained you on, please only read this part.  
If you want to track animals other than fish, please refer to the back part of this document.

### 1. Preliminary preparations  
a. Install git  
https://gitforwindows.org/  
b. Install anaconda  
https://www.anaconda.com/download  
c. Prepare the video you want to track  
mp4 is recommended for video format

### 2. preliminary operations
a. Launch a command prompt and type the following text

    git clone https://github.com/huqingrui/ultralytics_fish_tracking.git

b. Place the video files you want to analyze in the following folder  

    (directory downloaded by git)/fishtracking/video

### 3. Perform actual operation tracking

Start anaconda prompt and type the following text

    conda create -n yolo8

    conda activate yolo8　

    pip install ultralytics

    cd (the directory where you downloaded the git file)/fishtracking

    python fish_tracker.py

Tracking results are stored in "fishtracking/run"

## How to use the training program
If you prefer to do training by yourself, please do this part before doing part 3 above


#### 1. Prepare files for training  
* Prepare 10000 images cut from video data 
* Prepare a file with the coordinates of the location you want to track for each image.

#### 2. Move the created files to the following directories  
* images/train -> datasets/images/train   7000images
* images/val -> datasets/images/val       3000images
* labels/train -> datasets/labels/train
* labels/val -> datasets/labels/val

#### 3. Type the following text on anaconda prompt 

    yolo train data=fishtracking/test/datasets/Fish.yaml model=yolov8l.pt epochs=200 lr0=0.01 batch=128

#### 4. Move the output file (best.bt) to the folder  
 folder directory:  

     (the directory where you downloaded the git file)/fishtracking  

 rename or delete the file with the same name that preceded it
