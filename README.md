# April_Tag
This is a project for the 2023 CityU underwater robotics Fall Training **Task 1.2 Investigate the underwater environment.**

# How the code works
1. The code begins by importing the necessary libraries: `copy`, `time`, `argparse`, `cv2` (OpenCV), and `Detector` from `pupil_apriltags`.

2. The `get_args()` function is defined to handle command-line arguments. It creates an instance of the `argparse.ArgumentParser` class and adds several arguments related to the AprilTag detection. These arguments specify the device index, capture width and height, AprilTag families, number of threads, quad decimation factor, quad sigma, edge refinement, decode sharpening, and debug mode. The function parses the command-line arguments and returns an object containing the argument values.

3. The `main()` function is the program's entry point. It starts by calling `get_args()` to obtain the command-line arguments and assigns them to variables for easier access.

4. The program initializes the camera capture by creating a `VideoCapture` object (`cap`). It sets the frame width and height based on the provided arguments.

5. An instance of the `Detector` class is created (`at_detector`) with the specified AprilTag families, number of threads, quad decimation factor, quad sigma, edge refinement, decode sharpening, and debug mode.

6. The program enters a while loop that continuously captures frames from the camera. It reads a frame (`image`) using `cap.read()` and checks if the frame was successfully read (`ret` is `True`).

7. A copy of the captured frame (`debug_image`) is made for drawing purposes.

8. The captured frame is converted to grayscale using `cv.cvtColor()`.

9. The `at_detector.detect()` method is called to detect AprilTags in the grayscale image. The detected tags are stored in the `tags` variable.

10. The `draw_tags()` function is called to draw the detected tags on the `debug_image`. The function takes the `debug_image`, the detected tags (`tags`), and the elapsed time as arguments.

11. The elapsed time for processing the frame is calculated by subtracting the start time from the current time.

12. The program checks if the ESC key (key code 27) is pressed. If so, it breaks out of the while loop and ends the program.

13. The `debug_image` with the drawn tags is displayed using `cv.imshow()`.

14. Once the while loop is exited (either by pressing ESC or when no more frames are available), the camera capture is released and all OpenCV windows are destroyed.

15. The `draw_tags()` function takes the `image`, `tags`, and `elapsed_time` as arguments. It iterates over each detected tag and extracts the necessary information such as the tag family, tag ID, center coordinates, and corner coordinates.

16. The center and corner coordinates are converted to integers.

17. The function draws a circle at the center of the tag using `cv.circle()`.

18. It also draws lines to connect the corners of the tag using `cv.line()`.

19. The function adds text to the image to display the tag ID and the elapsed time.

20. Finally, the modified image is returned.

21. The `if __name__ == '__main__':` block ensures that the `main()` function is called only when the script is run directly, not when it is imported as a module.
