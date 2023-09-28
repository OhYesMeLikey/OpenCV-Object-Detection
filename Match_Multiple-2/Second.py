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
#print(result)

# Set a threshold for the resulting confidence values and print out the locations
threshold = 0.7
locations = np.where(result >= threshold)
print("locations\n", locations)

# Zip up the locations into position tuples
# The "star" symbol unpacks the list, and the "zip" keyword merges lists into new lists of each items that's at the same index
# In this case, the "locations" list gets reversed, removes the outermost list and gives multiple 1D lists, 
# go through each element per index and put them individually into a new list, and lastly, all the newly generated lists gets
# combined into one large list 

locations = list(zip(*locations[::-1]))
print("zipped up locations\n", locations)
