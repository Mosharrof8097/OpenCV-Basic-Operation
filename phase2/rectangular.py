import cv2

image = cv2.imread ("phase2\\mosh_gray.jpg")

if image is None:
    print("Opps! image is not working ")

else:
    print("Image is loading is succesfully ")

    p1=(1300,1300)   #staring point for line 
    p2=(2500,2500)   # ending for linning 
    color=(0,0,255) #color channel
    thikness=6         #line thikness 
    cv2.rectangle(image,p1,p2,color,thikness)   #line function which include picture varibale ,p1,p2,colro channel,thikness 
    cv2.imwrite("rectangle_image.jpg",image)

    cv2.imshow("After line image is ",image )
    cv2.waitKey(0)
    cv2.destroyAllWindows()

