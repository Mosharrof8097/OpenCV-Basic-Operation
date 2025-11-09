import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   # Windows stable driver

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not responding!")
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1)

    # q চাপলে break
    if key != -1:
        if chr(key) == 'q':
            break

cap.release()
cv2.destroyAllWindows()
