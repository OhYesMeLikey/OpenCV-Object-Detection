import cv2 as cv
import numpy as np
import os
import pyautogui

# Change the working directory to the folder that this script is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    screenshot = pyautogui.screenshot()
    # Convert the screenshotted image and assign it back to the 'screenshot' variable.
    screenshot = np.array(screenshot)
    # Convert RGB to BGR.
    # Without the following code, opencv will display multiple different colour screenshots.
    # screenshot = screenshot[:, :, ::-1].copy()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow("Computer Vision", screenshot)

    # Press 'q' with the output window focused to exit.
    # Waits for 1 ms every loop to check for key press.
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Done.")
