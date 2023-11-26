This is a fish tracking code based on the Ultralytics code https://github.com/ultralytics/ultralytics

How to use it 

1. Split the part1 video into each frame, take the first 10000 frames for yolov8 training, of which 7000 frames are the training set, and the last 3000 frames are the test and val set.

2. The path where the image is stored is shown below.

   ```
   <yolo8_home>
     |--ultralytics
     	|--datasets
     	  |--fish_yolo8
     	    |--images
     	       |--train
     	          |--frame_xxx.jpg ...(train imgs)
     	       |--val
     	          |--frame_xxx.jpg ...(val imgs)
     	    |--labels
     	       |--train
     	          |--frame_xxx.txt ...(train labels)
     	       |--val
     	          |--frame_xxx.txt ...(val labels)
   ```

3. create the <yolo8_home>/ultralytics/datasets/Fish.yaml file as shown.

   ```
   path: <yolo8_home>/ultralytics/datasets/fish_yolo8
   train: # train images (relative to 'path')  7000 images
     - images/train
     - images/val
   val: # val images (relative to 'path')  3000 images
     - images/val
   test: # test images (optional)
     - images/val
   # Classes
   names:
     0: fish
   ```

4. training

   ```
   -conda activate yolo8
   -yolo train data=<yolo8_home>/ultralytics/datasets/Fish.yaml model=yolov8l.pt epochs=200 lr0=0.01 batch=128
   ```

5. The weight file is generated in <yolo8_home>/runs/detect/train_xx after the training is completed.

6. create  the <yolo8_home>/tests/fish_tracker.py file as shown.

   ```
   model = YOLO('<yolo8_home>/runs/detect/train_xx/weights/best.pt')  # Load an official Detect model
   results = model.track(source="<yolo8_home>/videos/development.mp4", show=False, tracker="bytetrack.yaml", save_txt=True, save=True, save_conf=True)  # Tracking with ByteTrack tracker
   ```

7. The output file will be generated at <yolo8_home>/runs/detect/track_xx when finished.

8. Run the format conversion code("<yolo8_home>/tests/tran_mot_challenge.py") to convert the format to the MOT challenge format.

9. In addition, you can use scripts/trans_point2box.py to change the raw point data to box data
