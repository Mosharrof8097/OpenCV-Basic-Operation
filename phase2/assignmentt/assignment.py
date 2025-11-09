import cv2

def show_image(image, window_name=None):
    if window_name is None:
        window_name = input("Enter window name: ").strip() or "Image"
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread("phase2\\mosh.jpg")

if image is None:
    print("Image is not working properly")

else:
    print("iamge is loading succesfully")

    Operation=[
        "1.dimention",
        "2.roated",
        "3.flip",
        "4.draw_line",
        "5.draw_circle",
        "6.draw_rectangular",
        "7.Text_added",
        "8.crop",
        "9.resize",
        "10.grapy"
    ]
    for item in Operation:
        print(item)
    
    choice = int(input("Enter your choice: "))
    match choice:
      case 1:
            print("Dimention determine:")
            h,w,c = image.shape
            print(f"Image loaded:\nheight:{h}\nwidth:{w}\ncolor chnanel:{c}")
            show_image(image)
      case 2:
            print("Rotation Operation")
            (h,w)  = image.shape[:2] 
            center=(w/2,h/2)
            angle=float(input("Enter your angle in degre  : "))
            scal=float(input("Enter your scal  in float: "))
            
            M= cv2.getRotationMatrix2D(center,angle,scal)
            rotated=cv2.warpAffine(image,M,(w,h))
            show_image(rotated)
            
      case 3:
           print("Flip options:")
           print("1. Vertical flip")
           print("2. Horizontal flip")
           print("3. Both flip")

           flipChoice = int(input("Enter your flipping option number: "))

           match flipChoice:
            case 1:
              Vertical_flip = cv2.flip(image, 0)
              show_image(Vertical_flip)
            case 2:
              Horizontal_flip = cv2.flip(image, 1)
              show_image(Horizontal_flip)
            case 3:
               Both_flip = cv2.flip(image, -1)
               show_image(Both_flip)


      case  4:
            print("draw a Line into a image ")
            
            x1, y1 = map(int, input("Enter staring  coordinates x1,y1: ").split(","))
            p1 = (x1, y1)
            x2, y2 = map(int, input("Enter ending  coordinates x2,y2: ").split(","))
            p2 = (x2, y2)
            B,G,R= map(int,input("Enter the color channel 0-255(Blue,Green,Red):").split(","))
            color=(B,G,R)
            thikness=int (input("Enter the word thikness"))
            cv2.line(image,p1,p2,color,thikness)
            show_image(image)
      case 5:
            print("draw circile in a image ")
            x1, y1 = map(int, input("Enter center   coordinates x1,y1: ").split(","))
            center = (x1, y1)
            B,G,R= map(int,input("Enter the color channel 0-255(Blue,Green,Red):").split(","))
            color=(B,G,R)
            radious=int(input("Enter the radious of circle : "))
            thikness=int (input("Enter the word thikness"))

            cv2.circle(image,center,radious,color,thikness)
            show_image(image)
      case 6:
            print("draw rectangular")
            
            x1, y1 = map(int, input("Enter staring  coordinates x1,y1: ").split(","))
            p1 = (x1, y1)
            x2, y2 = map(int, input("Enter ending  coordinates x2,y2: ").split(","))
            p2 = (x2, y2)
            B,G,R= map(int,input("Enter the color channel 0-255(Blue,Green,Red):").split(","))
            color=(B,G,R)
            thikness=int (input("Enter the word thikness"))
            cv2.line(image,p1,p2,color,thikness)
            cv2.rectangle(image,p1,p2,color,thikness)
            show_image(image)
      case 7:
            print("Add a text on your image ")
            Input_text=str(input("Enter your text:"))
            x1, y1 = map(int, input("Enter  orgazie coordinates x1,y1: ").split(","))
            p1 = (x1, y1)
            fontScal=float(input("Enter font scal: "))
            B,G,R= map(int,input("Enter the color channel 0-255(Blue,Green,Red):").split(","))
            color=(B,G,R)
            thikness=int (input("Enter the word thikness"))
            bold=int(input("enter Bolt size in integer: "))
            cv2.putText(image,Input_text,p1,cv2.FONT_HERSHEY_SIMPLEX,fontScal,color,thikness,bold)
            show_image(image)
      case 8:
              print("crop The image")   
              
              x1, y1, x2, y2 = map(int,input("Enter crop coordinates x1,y1,x2,y2: ").split(","))
              cord=(x1,y1,x2,y2)
              croping=image[y1:y2, x1:x2]
              show_image(croping)
      case 9:
            print("Resize the image ")  
            height=int(input("Enter the new height"))   
            width= int (input("Enter the new width"))
            image=cv2.resize(image,(width,height))  
            show_image(image) 
      case 10:
              print("gray scal the image ") 
              gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
              show_image(gray)


save_choice=input("Enter your choice (y/n):")
if save_choice.lower()=="y":
     Operation_file_name=input("Enter your saving file name(Example.extension(.jpg)): ")
     cv2.imwrite(Operation_file_name,image)
     print("image save succesfully")
else:
      print("Image not saved.")     
     


            
      
 



