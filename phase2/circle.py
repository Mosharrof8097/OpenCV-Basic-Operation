import cv2

image = cv2.imread ("phase2\\mosh_gray.jpg")

if image is None:
    print("Opps! image is not working ")

else:
    print("Image is loading is succesfully ")

   
    color=(0,0,220) #color channel
    thikness=6         #line thikness 
    cv2.circle(image,(1300,2200),400,color,thikness)  #line function which include picture varibale ,p1,p2,colro channel,thikness 
    cv2.imwrite("Circle_image.jpg",image)

    cv2.imshow("After line image is ",image )
    cv2.waitKey(0)
    cv2.destroyAllWindows

