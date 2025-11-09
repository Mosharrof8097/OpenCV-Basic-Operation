import cv2 

image = cv2.imread("E:\OpenCV\Phase1\mosh.jpg") 
#for image open and reading use varibale =cv2.imread(path)

if image is None:
    print("ERROR")
else:
    print("image Loaded succesfully")
