#!/bin/bash
#SBATCH -p ubuntu
#SBATCH -c 10
#SBATCH --gres=gpu:8 

zsh
bash
source /home/q_hu/workspace6/opt/anaconda3/etc/profile.d/conda.sh
# conda init bash
conda init
conda activate yolo8
## Execute the python script
# 200
yolo train data=/home/q_hu/workspace6/MOT/ultralytics/ultralytics/datasets/Jersey.yaml model=/home/q_hu/workspace6/MOT/ultralytics/yolov8l.pt epochs=1000 lr0=0.01 device='0,1,2,3,4,5,6,7' batch=64
# 1000
# yolo train data=/home/q_hu/workspace6/MOT/ultralytics/ultralytics/datasets/Jersey.yaml model=/home/q_hu/workspace6/MOT/ultralytics/yolov8l.pt epochs=1000 lr0=0.01 batch=256 device='0,1,2,3,4,5,6,7'
