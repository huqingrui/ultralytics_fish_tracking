Handling instructions for beginners

１.事前準備
a.gitをインストールする
https://gitforwindows.org/

b.アナコンダをインストールする


c.トラッキングしたい動画を用意する


２．ベースとなるファイルのダウンロード
cd xxxxx
git clone xxxxx

学習用ファイルのダウンロード（自分で学習からやりたいひとのみ）
xxxxxxx


３．ファイルを整理

それぞれ以下のディレクトリへと移す
images/train -> datasets/images/train
images/val -> datasets/images/val
labels/train -> datasets/labels/train
labels/val -> datasets/labels/val

トラッキングしたい動画は以下の場所に置き、名前をsample.mp4に変える
fishtracking/video


３．実際の操作
トラッキングを行う

anaconda prompt　を起動

conda activate yolo8　
と入力

pip install ultralytics
と入力

cd （gitファイルをダウンロードしたディレクトリのパス）
と入力

python fishtracking/fish_tracker.py
と入力

自分で学習をやりたいひとのみ
anaconda prompt　を起動

conda activate yolo8　
と入力

pip install ultralytics
と入力

cd （gitファイルをダウンロードしたディレクトリのパス）
と入力

yolo train data=fishtracking/test/datasets/Fish.yaml model=yolov8l.pt epochs=200 lr0=0.01 batch=128
と入力

python fishtracking/fish_tracker.py
と入力