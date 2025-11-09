import cv2

image= cv2.imread("phase2\\mosh_gray.jpg")

if image is None:
    print("Image is not found ")

else:
    print("Image is loaded")  
    (h,w)  = image.shape[:2] #need h and w slicing

    center=(w/2,h/2)   #how to rotated in center 

    M=cv2.getRotationMatrix2D(center,90,1.0) # getRotationMatrix2D() rotation-এর formula তৈরি করে।

    rotated=cv2.warpAffine(image,M,(w,h)) #warpAffine() ফাংশন ম্যাট্রিক্স অনুযায়ী ছবিটিকে rotate করে।
    
    cv2.imwrite("roated_image.jpg",rotated)
     
    cv2.imshow("rorated image ",rotated)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows