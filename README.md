Handling instructions for beginners

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



