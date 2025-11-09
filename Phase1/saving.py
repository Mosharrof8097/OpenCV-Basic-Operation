import cv2 

image = cv2.imread("E:\\OpenCV\\Phase1\\mosh.jpg")   # use double (// )for address 

if image is not None:
    succes =cv2.imwrite("Output_mosh.png",image)  # for savig image 
    if succes:
        print("image save succesfully")
    else:
        print("faild to save image ") 

else:
    print("image not found")          