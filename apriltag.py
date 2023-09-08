import copy
import time
import argparse
import cv2 as cv
from pupil_apriltags import Detector


def get_args(): #Get april_tag type and default device
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", type=int, default=0) 
    parser.add_argument("--width", help='cap width', type=int, default=960) #width of the capture 960
    parser.add_argument("--height", help='cap height', type=int, default=540) #height of the capture 540
    parser.add_argument("--families", type=str, default='tag36h11')  #default april tag families 
    parser.add_argument("--nthreads", type=int, default=1) #number of threads
    parser.add_argument("--quad_decimate", type=float, default=2.0) #factor for quad detection
    parser.add_argument("--quad_sigma", type=float, default=0.0) #sigma for quad decimation
    parser.add_argument("--refine_edges", type=int, default=1)
    parser.add_argument("--decode_sharpening", type=float, default=0.25)
    parser.add_argument("--debug", type=int, default=0)
    args = parser.parse_args()
    return args

def draw_tags(
    image,
    tags,
    elapsed_time,
):
    for tag in tags:
        tag_family = tag.tag_family
        tag_id = tag.tag_id
        center = tag.center
        corners = tag.corners

        center = (int(center[0]), int(center[1]))
        corner_01 = (int(corners[0][0]), int(corners[0][1]))
        corner_02 = (int(corners[1][0]), int(corners[1][1]))
        corner_03 = (int(corners[2][0]), int(corners[2][1]))
        corner_04 = (int(corners[3][0]), int(corners[3][1]))

        # Draw a circle at the center of the tag
        cv.circle(image, (center[0], center[1]), 5, (0, 0, 255), 2)

        # Draw lines to connect the corners of the tag
        cv.line(image, (corner_01[0], corner_01[1]),
                (corner_02[0], corner_02[1]), (255, 0, 0), 2)
        cv.line(image, (corner_02[0], corner_02[1]),
                (corner_03[0], corner_03[1]), (255, 0, 0), 2)
        cv.line(image, (corner_03[0], corner_03[1]),
                (corner_04[0], corner_04[1]), (0, 255, 0), 2)
        cv.line(image, (corner_04[0], corner_04[1]),
                (corner_01[0], corner_01[1]), (0, 255, 0), 2)


        # cv.putText(image,
        #            str(tag_family) + ':' + str(tag_id),
        #            (corner_01[0], corner_01[1] - 10), cv.FONT_HERSHEY_SIMPLEX,
        #            0.6, (0, 255, 0), 1, cv.LINE_AA)
        # Draw the tag ID
        cv.putText(image, str(tag_id), (center[0] - 10, center[1] - 10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv.LINE_AA)

    # Draw the elapsed time on the image
    cv.putText(image,
               "Elapsed Time:" + '{:.1f}'.format(elapsed_time * 1000) + "ms",
               (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
               cv.LINE_AA)

    return image

def main():
    # Get the command-line arguments
    args = get_args()

    #Extract the arguments
    cap_device = args.device
    cap_width = args.width
    cap_height = args.height
    families = args.families
    nthreads = args.nthreads
    quad_decimate = args.quad_decimate
    quad_sigma = args.quad_sigma
    refine_edges = args.refine_edges
    decode_sharpening = args.decode_sharpening
    debug = args.debug

    #Initialize the camera
    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    # Initialze Detector
    at_detector = Detector(
        families=families,
        nthreads=nthreads,
        quad_decimate=quad_decimate,
        quad_sigma=quad_sigma,
        refine_edges=refine_edges,
        decode_sharpening=decode_sharpening,
        debug=debug,
    )

    elapsed_time = 0

    while True:
        start_time = time.time()

        #Read frame
        ret, image = cap.read()
        if not ret:
            break
        debug_image = copy.deepcopy(image) #Create copy of the image for debugging purposes

        #covert image to grayscale
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        #Detact Apriltags
        tags = at_detector.detect(
            image,
            estimate_tag_pose=False,
            camera_params=None,
            tag_size=None,
        )

        ## Draw tags on the image
        debug_image = draw_tags(debug_image, tags, elapsed_time)

        elapsed_time = time.time() - start_time

        # Stop the program when ESC key is pressed
        key = cv.waitKey(1)
        if key == 27:  # ESC
            break

        # Display the image with AprilTags
        cv.imshow('AprilTag Detect Demo', debug_image)

    cap.release()
    cv.destroyAllWindows()

# Ensures that the `main()` function is called only when the script is run directly, not when it is imported as a module.
if __name__ == '__main__': 
    main()