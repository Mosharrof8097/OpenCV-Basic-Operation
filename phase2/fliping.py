import cv2

image = cv2.imread("phase2\\mosh_gray.jpg")

if image is None:
    print("Image is not found ")

else:
    print(" image is loaded ")

    vertical_rotation = cv2.flip(image,0)#0 → vertical (উপর ↕️ নিচে উল্টানো)
    horigontal_rotation= cv2.flip(image ,1)#1 → horizontal (ডান ↔️ বামে উল্টানো)
    both_rotation=cv2.flip(image ,-1)#-1 → both vertical & horizontal
       #saving image 
    cv2.imwrite("vertical_image.jpg",vertical_rotation)
    cv2.imwrite("horigontal_image.jpg",horigontal_rotation)
    cv2.imwrite("BothR_image.jpg",both_rotation)
     
     #showing iamge 

    cv2.imshow("vertical_image.jpg",vertical_rotation)
    cv2.imshow("horigontal_image.jpg",horigontal_rotation)
    cv2.imshow("BothR_image.jpg",both_rotation)
    
    #wait and destroy
    cv2.waitKey(0)
    cv2.destroyAllWindows

