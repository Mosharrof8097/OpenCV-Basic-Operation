import cv2

image = cv2.imread ("phase2\\mosh_gray.jpg")

if image is None:
    print("Opps! image is not working ")

else:
    print("Image is loading is succesfully ")

    cv2.putText(image,"Hi Mosharrof",(1300,1800),cv2.FONT_HERSHEY_SIMPLEX,6.5,(255,0,25),3,3)
    cv2.imwrite("Addtext_image.jpg",image)

   

    cv2.imshow("After adding text image is ",image )
    cv2.waitKey(0)
    cv2.destroyAllWindows()

