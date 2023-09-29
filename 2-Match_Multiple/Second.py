#! C:\Users\leota\Desktop\OpenCV Object Detection\myenv\Scripts\python.exe
import cv2 as cv
import numpy as np


source_img = cv.imread("TheRange.jpg", cv.IMREAD_UNCHANGED)
target_img = cv.imread("Bot.jpg", cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(source_img, target_img, cv.TM_CCOEFF_NORMED)

threshold = 0.7

# Returns a new numpy list of all possible confidence values that are bigger than the set threshold value
locations = np.where(result >= threshold)

# Zip up the locations into position tuples
# The "star" symbol unpacks the list, and the "zip" keyword merges lists into new lists of each items that's at the same index
# In this case, the "locations" list gets reversed, removes the outermost list and gives multiple 1D lists,
# go through each element per index and put them individually into a new list, and lastly, all the newly generated lists gets
# combined into one large list
locations = list(zip(*locations[::-1]))
# print("Locations\n", locations)

# Check if there is a list of locations
if locations:
    print("Found good matches")

    target_w = target_img.shape[1]
    target_h = target_img.shape[0]
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    # Loop through each location and draw their rectangle
    for loc in locations:
        top_left = loc

        bottom_right = (top_left[0] + target_w, top_left[1] + target_h)

        cv.rectangle(source_img, top_left, bottom_right, line_color, line_type)

    cv.imshow("Result", source_img)

    cv.waitKey()

    cv.imwrite("Result.png", source_img)
else:
    print("No good matches")
