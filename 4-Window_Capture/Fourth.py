import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time

# Changes the working directory to the folder that this script is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Marks down the current time before entering the loop.
loop_time = time()
while True:
    screenshot = pyautogui.screenshot()
    # Converts the screenshotted image and assign it back to the 'screenshot' variable.
    screenshot = np.array(screenshot)

    # Converts RGB to BGR.
    # Without the following code, opencv will display multiple different colour screenshots.
    # screenshot = screenshot[:, :, ::-1].copy()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow("Computer Vision", screenshot)

    # Prints out the FPS
    print("FPS {}".format(1 / (time() - loop_time)))
    loop_time = time()

    # Press 'q' with the output window focused to exit.
    # Waits for 1 ms every loop to check for key press.
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Done.")
