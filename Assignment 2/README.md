# CSc 8830: Computer Vision : Assignment 2 Solutions

## Question 1

The solution can be found in the the file 'q1.ipynb'

The code prompts the user to take a 10 seconds video. The video frames are stored in the folder "video_frames".

A random image was chosen from the video frames to perform CANNY EDGE DETECTION and stored in canny_edge_detection.png.

<img src="Assignment 2/canny_edge_detection.png" alt="Canny Edge Detection">

___

## Question 2

Similar to Question 1, The Harris corner detection algorithm was manually applied to a 5x5 image patch within a selected region containing a corner of interest. 

The detected corner pixels were noted and compared with automated implementations using DepthAI's Harris corner detection function for a comprehensive analysis.

The solution can be found in the the file 'q2.ipynb'

<img src="Assignment 2/harris_corner_detection.png" alt="Canny Edge Detection">

___

## Question 3

The SIFT feature extraction and matching algorithm was implemented to compute the sum of squared differences (SSD) between corresponding super-pixel patches in two images from the 'video_frames' separated by at least 2 seconds with some scene overlap.

The Homography matrix was also computed between these images, along with its inverse, using Python implementation.

The solution can be found in the the file 'q3.ipynb'

<img src="Assignment 2/homography.png" alt="Canny Edge Detection">

___

## Question 4

The code computes and displays the integral image feed alongside the RGB feed without relying on built-in functions such as "output = integral_image(input)".

The implementation initializes the integral image to zero, copies pixel values from the grayscale image, and calculates the integral image using the integral image algorithm.

### Integral Image Matrix
[Integral Image Matrix File](Assignment2/integral_matrix.txt)


### Integral Image Display for Frame.jpg
<img src="Assignment 2/integral_image_display.png" alt="integral_image">

___

## Question 5

The image stitching functionality for creating a 360-degree panoramic output in real-time was successfully implemented, utilizing SIFT or ORB features. 

The implementation involved constructing panoramas from images of home and science buildings without utilizing built-in functions directly performing image stitching.


Below are the images of Home Buildings used: 
<table>
  <tr>
    <td><img src="Assignment 2/image_stitching/building3.jpg" alt="Building 3"></td>
    <td><img src="Assignment 2/image_stitching/building2.jpg" alt="Building 2"></td>
    <td><img src="Assignment 2/image_stitching/building1.jpg" alt="Building 1"></td>
  </tr>
</table>

Below are the images of Science Center used: 

<table>
  <tr>
    <td><img src="Assignment 2/image_stitching/sciencecenter1.jpg" alt="Building 3"></td>
    <td><img src="Assignment 2/image_stitching/sciencecenter2.jpg" alt="Building 2"></td>
    <td><img src="Assignment 2/image_stitching/sciencecenter3.jpg" alt="Building 1"></td>
  </tr>
</table>

### Home Buildings ORB Stitching : 

<img src="Assignment 2/image_stitching/ORB1.jpg" alt="ORB1.jpg">

### Home Buildings ORB Stitching, other buildings : 

<img src="Assignment 2/image_stitching/ORB2.jpg" alt="ORB2.jpg">

### Home Buildings SIFT Stitching : Panaroma : 

<img src="Assignment 2/image_stitching/building_stiched.jpg" alt="building_stiched.jpg">

### Science Center SIFT Stitching : Panaroma : 

<img src="Assignment 2/image_stitching/sciencecent_stiched.jpg" alt="sciencecent_stiched.jpg">




