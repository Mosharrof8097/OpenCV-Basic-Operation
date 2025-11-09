import cv2 

# Load the image
image = cv2.imread("Phase1\\mosh.jpg")

# Check if the image was loaded
if image is not None:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show both images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)

    # Wait for key press
    cv2.waitKey(0)

    # Destroy all windows
    cv2.destroyAllWindows()

    # Save grayscale image
    cv2.imwrite("Phase1\\mosh_gray.jpg", gray)

else:
    print("Image not found. Check the file path!")
