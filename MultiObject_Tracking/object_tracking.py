import cv2
import numpy as np
from object_detection import ObjectDetection
import math

# Initialize Object Detection
od = ObjectDetection()

# setup video capture
cap = cv2.VideoCapture("los_angeles.mp4")
frame_number = 0

center_points_prev_frame = []
tracking_objects = {}
track_id = 0

while True:
    # read the frame. If there are no frames left, break the loop
    result, frame = cap.read()
    frame_number += 1
    if not result:
        break

    # center points of the bounding boxes in the current frame
    # - note that is why it is put in the while loop, so it only has current frames points
    center_points_cur_frame = []

    # Detect objects on frame
    # - class_ids: what the object is (car, truck, etc)
    # - scores: confidence of detection
    # - boxes: bounding box of location of each object
    class_ids, scores, boxes = od.detect(frame)

    for box in boxes:
        # a box has 4 numbers in total: x, y of top left corner, then width and height.
        x, y, w, h = box
        # print("FRAME #", frame_number, " ", x, y, w, h)

        # draw rectangle bounding boxes around the detected objects in the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # get center coordinates of the box
        center_x = int(x + int(w / 2))
        center_y = int(y + int(h / 2))
        # cv2.circle(frame, (center_x, center_y), 5, (0,0,255), -1)

        # append the center coordinates to a list
        center_points_cur_frame.append((center_x, center_y))

    # Only at the beginning we compare previous and current frame
    if frame_number <= 2:
        for point in center_points_cur_frame:
            for point_prev in center_points_prev_frame:
                distance = math.hypot(
                    point_prev[0] - point[0], point_prev[1] - point_prev[1]
                )

                if distance < 20:
                    tracking_objects[track_id] = point
                    track_id += 1
    else:

        tracking_objects_copy = tracking_objects.copy()
        center_points_cur_frame_copy = center_points_cur_frame.copy()
        
        for object_id, point_prev in tracking_objects_copy.items():
            
            object_exists = False
            
            for point in center_points_cur_frame_copy:
 
                distance = math.hypot(
                    point_prev[0] - point[0], point_prev[1] - point_prev[1]
                )

                # update ID's position
                if distance < 20:
                    tracking_objects[object_id] = point
                    object_exists = True
                    if point in center_points_cur_frame:
                        center_points_cur_frame.remove(point)
                    continue
            
            # Remove id if object has gone off the screen or is no longer being tracked
            if not object_exists:
                tracking_objects.pop(object_id)

        # Add new IDs found
        for point in center_points_cur_frame:
            tracking_objects[track_id] = point
            track_id += 1

    for object_id, point in tracking_objects.items():
        cv2.circle(frame, point, 5, (0, 0, 255), -1)
        cv2.putText(
            frame, str(object_id), (point[0], point[1] - 7), 0, 1, (0, 0, 255), 1
        )

    # print("Tracking objects")
    # print(tracking_objects)

    # print("CUR FRAME LEFT POINTS")
    # print(center_points_cur_frame)
    # print("PREV FRAME")
    # print(center_points_prev_frame)

    cv2.imshow("Frame", frame)

    # Make a copy of the points (make current points become the new previous points)
    center_points_prev_frame = center_points_cur_frame.copy()

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
