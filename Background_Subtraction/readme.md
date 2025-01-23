# Background Subtraction
## The Process
1. The camera is not moving, it is pointed at a road with moving cars. We want to show only the moving cars
2. We first do background estimation, where we find what the background looks like (the road) without any moving cars:
   - Every pixel sees the same piece of the background because the camera is not moving. Occasionally, a moving car obscures the background.
   - We randomly sample a few frames from the video to get estimates of the background. As long as a pixel is not covered by a moving car more than 50% of the time, the median of the pixel over these sample frames will give a good estimate of the background at that pixel.
   - We can repeat this for every pixel and recover the entire background.
3. Now we do background subtraction (now we show only the cars). We can create a mask for every frame which shows parts of the image that are in motion.
   - Convert the median frame to grayscale.
   - Loop over all frames in the video. Extract the current frame and convert it to grayscale.
   - Calculate the absolute difference between the current frame and the median frame.
   - Threshold the above image to remove noise and binarize the output (convert image to black and white).
4. Done!


## Links
- Based on [LearnOpenCV](https://learnopencv.com/simple-background-estimation-in-videos-using-opencv-c-python/)