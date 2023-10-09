#!/bin/bash
#SBATCH -p ubuntu
#SBATCH -c 10
#SBATCH --gres=gpu:4 
#SBATCH -x tesla
#SBATCH -w aventador
zsh
bash
source /home/q_hu/workspace6/opt/anaconda3/etc/profile.d/conda.sh
# conda init bash
conda init
conda activate yolo8
## Execute the python script
yolo train data=/home/q_hu/workspace6/MOT/ultralytics/ultralytics/datasets/Jersey.yaml model=/home/q_hu/workspace6/MOT/ultralytics/yolov8l.pt epochs=200 lr0=0.01 device='0,1,2,3' batch=256
