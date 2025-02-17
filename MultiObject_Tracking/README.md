# MultiObject Tracking (MOT)
Tracks and ID's multiple vehicles in a video.

See the [Links](#links) section for the tutorial I followed.

## Process Breakdown
1. Detect the vehicles in each frame of the video using the object detection model
2. Draw bounding boxes around each vehicle (note that a bounding box of a certain car in 1 frame, has no relation to the bounding box of the same car in the next frame)
3. Get the coordinates of the center of each bounding box
4. For each vehicle, we only care about 2 points at a time: the location of center of the bounding box in the current frame and the previous frame
5. Then we calculate the distance between the current and previous points. If the distance is small enough, we are tracking the same object!
6. Compare the previous object with the current one and update the position of the ID. This way, the same object remains with the same ID for its entire path. When the object is no longer recognized, it loses the ID.
7. If a new object is identified, the list of points must also be updated. 

## Other options
Other options include using the SORT or Deep SORT algorithms. By saving the position of the center point of each object, you can trace the previous position of the objects and predict what the immediate next will be.

## Links
- [ Object Tracking from scratch with OpenCV and Python | PySource](https://pysource.com/2021/10/05/object-tracking-from-scratch-opencv-and-python/)