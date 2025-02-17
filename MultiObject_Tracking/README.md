# MultiObject Tracking (MOT)

The idea is:
1. detect the vehicles in each frame of the video using the training object detection model
2. draw bounding boxes around each vehicle (note that a bounding box of a certain car in 1 frame, has no relation to the bounding box of the same car in the next frame)
3. get the coordinates of the center of each bounding box
4. for each vehicle, we only care about 2 points at a time: the location of center of the bounding box in the current frame and the previous frame
5. then we calculate the distance between the current and previous points. If the distance is small enough, we are tracking the same object!
6. we have to make sure to compare the previous object with the current one and update the position of the ID. In this way, the same object remains with the same ID for its entire path. When the object is no longer recognized, it loses the ID.
7. If a new object is identified, the list of points must also be updated. 


- By saving the position of the center point of each object, you can trace the previous position of the objects and predict what the immediate next will be
- 


## Links
- [ Object Tracking from scratch with OpenCV and Python - PySource](https://pysource.com/2021/10/05/object-tracking-from-scratch-opencv-and-python/)