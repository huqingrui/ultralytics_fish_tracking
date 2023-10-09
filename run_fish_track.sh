#!/bin/bash
#SBATCH -p ubuntu
#SBATCH -c 10
#SBATCH --gres=gpu:4
###SBATCH -x tesla
## #SBATCH -w aventador
bash
# conda init bash
conda init
conda activate yolo8
## Execute the python script
python ultralytics/tests/fish_tracker.py
