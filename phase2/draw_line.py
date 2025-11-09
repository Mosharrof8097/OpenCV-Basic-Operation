import cv2

image = cv2.imread ("phase2\\mosh_gray.jpg")

if image is None:
    print("Opps! image is not working ")

else:
    print("Image is loading is succesfully ")

    p1=(1000,1200)   #staring point for line 
    p2=(2000,2000)   # ending for linning 
    color=(255,225,30) #color channel
    thikness=6         #line thikness 
    cv2.line(image,p1,p2,color,thikness)   #line function which include picture varibale ,p1,p2,colro channel,thikness 
    cv2.imwrite("line_image.jpg",image)

    cv2.imshow("After line image is ",image )
    cv2.waitKey(0)
    cv2.destroyAllWindows()

