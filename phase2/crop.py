import cv2 

image = cv2.imread("phase2\\mosh_gray.jpg")

if image is None:
    print("Image is not found ")
else:
    croping = image[100:200,50:100]
    cv2.imshow("croping image ",croping)
    cv2.waitKey(0)
    cv2.destroyAllWindows()