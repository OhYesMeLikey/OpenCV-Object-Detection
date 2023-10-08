import cv2 as cv
import numpy as np
import os
from time import time
import win32gui, win32ui, win32con


# Changes the working directory to the folder that this script is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def window_capture():
    w = 2560  # set this
    h = 1440  # set this

    # hwnd = win32gui.FindWindow(None, windowname)
    hwnd = None

    # Get the window image data
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)

    # Save the screenshot
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype="uint8")
    img.shape = (h, w, 4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img


# Marks down the current time before entering the loop.
loop_time = time()
while True:
    # Obtains a screenshot from window_capture() that open cv can use right away
    screenshot = window_capture()

    cv.imshow("Computer Vision", screenshot)

    # Prints out the FPS.
    print("FPS {}".format(1 / (time() - loop_time)))
    loop_time = time()

    # Press 'q' with the output window focused to exit.
    # Waits for 1 ms every loop to check for key press.
    if cv.waitKey(1) == ord("q") or cv.waitKey(1) == ord("Q"):
        cv.destroyAllWindows()
        break

print("Done.")
