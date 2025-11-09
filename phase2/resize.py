import cv2

image = cv2.imread("phase2\\mosh_gray.jpg")

if image is None:
    print("Image is not found")
else:
    print("Image is loaded")   
    resize= cv2.resize(image,(300,300)) #width,height
    cv2.imshow("Original Image",image)
    cv2.imshow("resize Image",resize)

    cv2.imwrite("resize_output.jpg",resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
