import cv2 

image = cv2.imread("E:\OpenCV\Phase1\mosh.jpg")

if image is not None:
    cv2.imshow("showing image ",image) # showing image 
    cv2.waitKey(0) # until i any key press wait 
    cv2.destroyAllWindow() # destroy or close all window 
else:
    print("could not load the image ")    