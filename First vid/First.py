#! C:\Users\leota\Desktop\OpenCV Object Detection\First vid\myenv\Scripts\python.exe
import cv2 as cv
import numpy as np

# print("hello")

# Read the source file
source_img = cv.imread("TheRange.jpg", cv.IMREAD_UNCHANGED)
# Read the targe file
target_img = cv.imread("Bot.jpg", cv.IMREAD_UNCHANGED)

# Search and find the target in the source file
result = cv.matchTemplate(source_img, target_img, cv.TM_CCOEFF_NORMED)

# Returns the minimum and maximum values (i.e. blackest and whitest pixels, ranging from 0 to 1, where 0 is the darkest black and 1 is the brightest white)
# Returns the locations of those minimum and maximum values
# tldr; Returns the best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print("Best match top left position: %s" % str(max_loc))
print("Best match confidence: %s" % max_val)

threshold = 0.9
if max_val >= threshold:
    print("Found good match")

    # Get dimensions of the target image
    target_w = target_img.shape[1]
    target_h = target_img.shape[0]

    # Idk why top_left was assigned max_loc
    top_left = max_loc
    bottom_right = (top_left[0] + target_w, top_left[1] + target_h)

    # Draw a box around the target image
    cv.rectangle(
        source_img,
        top_left,
        bottom_right,
        color=(0, 255, 0),
        thickness=2,
        lineType=cv.LINE_4,
    )

    # Display the result
    cv.imshow("Result", source_img)

    # Pauses the code until we press a key
    cv.waitKey()
else:
    print("No good match")
