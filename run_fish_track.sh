#!/bin/bash
#SBATCH -p ubuntu
#SBATCH -c 10
#SBATCH --gres=gpu:4
###SBATCH -x tesla
## #SBATCH -w aventador
zsh
bash
source /home/q_hu/workspace6/opt/anaconda3/etc/profile.d/conda.sh
# conda init bash
conda init
conda activate yolo8
## Execute the python script
cd /home/q_hu/workspace6/MOT/ultralytics
python /home/q_hu/workspace6/MOT/ultralytics/tests/fish_tracker.py
