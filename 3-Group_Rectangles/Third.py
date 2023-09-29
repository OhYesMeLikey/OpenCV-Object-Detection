#! C:\Users\leota\Desktop\OpenCV Object Detection\myenv\Scripts\python.exe
import cv2 as cv
import numpy as np


source_img = cv.imread("TheRange.jpg", cv.IMREAD_UNCHANGED)
target_img = cv.imread("Bot.jpg", cv.IMREAD_UNCHANGED)

target_w = target_img.shape[1]
target_h = target_img.shape[0]

result = cv.matchTemplate(source_img, target_img, cv.TM_CCOEFF_NORMED)

threshold = 0.7
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))

# Create a list [x,y,w,h] rectangles
rectangles = []
for loc in locations:
    rect = [int(loc[0]), int(loc[1]), target_w, target_h]
    # Since the following function groupRectangles require at least two boxes to be considered as a "grouped" item,
    # a single rectangle will be added in twice, so the function groupRectangles will actually group up the two same single
    # boxes as a real result, instead of throwing it out
    rectangles.append(rect)
    rectangles.append(rect)


# Group the rectangles together from the given list,
# set the groupThreshold to 1 because 0 doesn't group any rectangles together, 2 or 3 require more overlapping rectangles to be effective,
# set the eps to 0.5 as a baseline number to judge how close the rectangles need to be in order to group them together,
# reassign the grouped up rectangles to the original rectangles list but "weights" won't be used
rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
print("Rectangles", rectangles)

# Checking the truth value of a list with multiple values is ambiguous, so it was replaced
# with checking the length of a list
if len(rectangles):
    print("Found good matches")

    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    for x, y, w, h in rectangles:
        top_left = (x, y)

        bottom_right = (x + w, y + h)

        cv.rectangle(source_img, top_left, bottom_right, line_color, line_type)

    cv.imshow("Result", source_img)

    cv.waitKey()

    cv.imwrite("Result.jpg", source_img)
else:
    print("No good matches")
