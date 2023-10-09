import cv2 as cv
import numpy as np


def findClickPositions(target_img_path, source_img, threshold, debug_mode=None):
    target_img = cv.imread(target_img_path, cv.IMREAD_UNCHANGED)

    target_w = target_img.shape[1]
    target_h = target_img.shape[0]

    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(source_img, target_img, method)

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
    points = []
    if len(rectangles):
        print("Found good matches")
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for x, y, w, h in rectangles:
            # Locate the center of each rectangle and draw a cross for each of them
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)

            # Save the points
            points.append((center_x, center_y))

            if debug_mode == "rectangles":
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                cv.rectangle(source_img, top_left, bottom_right, line_color, line_type)
            elif debug_mode == "points":
                cv.drawMarker(
                    source_img, (center_x, center_y), marker_color, marker_type
                )

    if debug_mode:
        cv.imshow("Result", source_img)
        # cv.waitKey()
        # cv.imwrite("Result.jpg", source_img)

    return points
