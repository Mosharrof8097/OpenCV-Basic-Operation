import cv2

image = cv2.imread("E:\\OpenCV\\Phase1\\mosh.jpg")

if image is not None:
    h,w,c = image.shape
    print(f"Image loaded:\n height:{h}\nwidth:{w}\n color chnanel:{c}")

else:
    print(" could not loading")   