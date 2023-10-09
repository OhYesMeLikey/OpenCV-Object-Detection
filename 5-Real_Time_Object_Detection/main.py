import cv2 as cv
import numpy as np
import os
from time import time
from window_capture import WindowCapture
from vision import Vision

# Changes the working directory to the folder that this script is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create an object from the WindowCapture class
# For valorant, there are two spaces after the name
wincap = WindowCapture("VALORANT  ")
# wincap = WindowCapture()
vision_bot = Vision("Bot.jpg")

# Marks down the current time before entering the loop.
loop_time = time()
while True:
    # Obtains a screenshot from get_screenshot() that open cv can use right away
    screenshot = wincap.capture_win_alt()
    # screenshot = wincap.get_screenshot()

    # Display the processed image
    vision_bot.find(screenshot, 0.5, "rectangles")

    # Prints out the FPS.
    print("FPS {}".format(1 / (time() - loop_time)))
    loop_time = time()

    # Press 'q' with the output window focused to exit.
    # Waits for 1 ms every loop to check for key press.
    if cv.waitKey(1) == ord("q") or cv.waitKey(1) == ord("Q"):
        cv.destroyAllWindows()
        break

print("Done.")
