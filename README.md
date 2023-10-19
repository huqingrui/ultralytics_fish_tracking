Handling instructions for beginners


1. Preliminary preparations
a.Install git
https://gitforwindows.org/

b.Install anaconda
https://www.anaconda.com/download

c.Prepare the video you want to track.
.mp4 is recommended for video format

2. preliminary operations
Launch a command prompt
Type the following text
    git clone https://github.com/huqingrui/ultralytics_fish_tracking.git

Place the video files you want to analyze in the following folder
(directory downloaded by git)/fishtracking/video


3. Perform actual operation tracking

Start anaconda prompt
Type the following text

    conda create -n yolo8

    conda activate yolo8　

    pip install ultralytics

    cd (the directory where you downloaded the git file)/fishtracking

    python fish_tracker.py

Tracking results are stored in　fishtracking/run


Only for those who want to do the learning by themselves
1. Prepare files for learning
Prepare files for training
Prepare 10000 images cut from video data
Prepare a file with the coordinates of the location you want to track for each image.

Move the created files to the following directories
images/train -> datasets/images/train   7000images
images/val -> datasets/images/val       3000images
labels/train -> datasets/labels/train
labels/val -> datasets/labels/val

Type the following text
    yolo train data=fishtracking/test/datasets/Fish.yaml model=yolov8l.pt epochs=200 lr0=0.01 batch=128


Move the output file (best.bt) to the following folder (rename or delete the file with the same name that preceded it)
(the directory where you downloaded the git file)/fishtracking


in Japanese

１.事前準備
a.gitをインストールする
https://gitforwindows.org/

b.アナコンダをインストールする
https://www.anaconda.com/download

c.トラッキングしたい動画を用意する
動画形式は.mp4を推奨

２．予備操作
コマンドプロンプトを起動
git clone https://github.com/huqingrui/ultralytics_fish_tracking.git

解析したい動画ファイルを以下のフォルダに置く
（gitでダウンロードしたディレクトリ）/fishtracking/video


３．実際の操作トラッキングを行う

anaconda prompt　を起動

conda create -n yolo8

conda activate yolo8　

pip install ultralytics

cd （gitファイルをダウンロードしたディレクトリ）/fishtracking

python fish_tracker.py

トラッキング結果は
fishtracking/run　に保存される


自分で学習をやりたいひとのみ

1.学習用ファイルの作成
学習用にファイルを準備する
動画データから切り取った画像を10000枚用意
それぞれに対してトラッキングしたい場所の座標を記入したファイルを

作成したファイルをそれぞれ以下のディレクトリへと移す
images/train -> datasets/images/train　
images/val -> datasets/images/val　
labels/train -> datasets/labels/train
labels/val -> datasets/labels/val

yolo train data=fishtracking/test/datasets/Fish.yaml model=yolov8l.pt epochs=200 lr0=0.01 batch=128
と入力

出力されたファイル（best.bt）を以下のフォルダへと移動（その前にあった同名のファイルは名前を変えるか削除する）
（gitファイルをダウンロードしたディレクトリ）/fishtracking



