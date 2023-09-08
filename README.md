# April_Tag
This is a project for the 2023 CityU underwater robotics Fall Training **Task 1.2 Investigate the underwater environment.**

# How the code works
1. The code starts by importing the necessary libraries, including copy, time, argparse, cv2 (OpenCV), and pupil_apriltags (a library for detecting AprilTags).

2. The get_args() function is defined to handle command-line arguments. It sets up an argument parser and defines various arguments such as the device number, capture width, capture height, AprilTag families, number of threads, and various detection parameters. The function returns the parsed arguments.

3. The draw_tags() function takes an image, a list of detected AprilTags, and the elapsed time as input. It iterates over each detected tag and extracts its properties such as tag family, tag ID, center, and corners. It then draws a circle at the center of the tag and lines to connect the corners. It also displays the tag ID and the elapsed time on the image. The function returns the modified image.

4. The main() function is the entry point of the program. It first calls the get_args() function to get the command-line arguments and extracts the relevant values.

5. It initializes the camera using the specified device number and sets the capture width and height.

6. It creates an instance of the AprilTag detector (at_detector) by passing the specified families, number of threads, and other detection parameters.

7. Inside the main loop, the program reads a frame from the camera using the cap.read() function. If the frame is not successfully read, the loop breaks.

8. The frame is then deep-copied to create a separate image (debug_image) for debugging purposes.

9. The color image is converted to grayscale using cv.cvtColor().

10. The AprilTags are detected in the grayscale image using the at_detector.detect() function. This function returns a list of detected tags.

11. The draw_tags() function is called to draw the detected tags on the debug_image along with the elapsed time.

12. The elapsed time for processing the frame is calculated.

13. The program checks if the ESC key is pressed. If so, it breaks the loop.

14. The debug_image with the AprilTags is displayed using cv.imshow().

15. Once the loop ends (e.g., when the ESC key is pressed), the camera is released and all OpenCV windows are destroyed.

16. The program execution ends.
