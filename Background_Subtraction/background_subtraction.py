import numpy as np
import cv2
# from skimage import data, filters
 
# Open Video
video = cv2.VideoCapture('video.mp4')
 
# ***BACKGROUND ESTIMATION:***

# Randomly select 25 frames
# frameIds is a numpy array
frameIds = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)
 
# Store selected frames in an array
frames = []
for fid in frameIds:
    video.set(cv2.CAP_PROP_POS_FRAMES, fid) # set frame number in the video
    result, frame = video.read() # video.read() returns a bool and the frame
    frames.append(frame) # add to array
 
# Calculate the median along the time axis
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)    
 
# Display median frame
cv2.imshow('Estimated background', medianFrame)
cv2.waitKey(0)

# ***BACKGROUND SUBTRACTION: (frame differencing):***

# Reset frame number to 0
video.set(cv2.CAP_PROP_POS_FRAMES, 0)
 
# Convert background to grayscale
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)
 
# Loop over all frames
result = True
while(result):
  # Read frame
  result, frame = video.read()

  # Convert current frame to grayscale
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  # Calculate absolute difference of current frame and the median frame
  differenceFrame = cv2.absdiff(frame, grayMedianFrame)

  # Threshold to binarize
  threshold, differenceFrame = cv2.threshold(differenceFrame, 30, 255, cv2.THRESH_BINARY)

  # Display image
  cv2.imshow('Subtracted video', differenceFrame)
  cv2.waitKey(20)
 
# Release video object
video.release()
 
# Destroy all windows
cv2.destroyAllWindows()