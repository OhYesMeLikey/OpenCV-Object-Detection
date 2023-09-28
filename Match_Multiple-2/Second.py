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


