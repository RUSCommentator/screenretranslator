import cv2
screen_capture = cv2.VideoCapture(0)
while True:
    ret, frame = screen_capture.read()
    if not ret:
        break
    
    #folder_path = input("Enter folder path ")
    cv2.imshow('Screen Capture', frame)
    cv2.waitKey(1)

    if cv2.getWindowProperty('Screen Capture', cv2.WND_PROP_VISIBLE) < 1:
        break

screen_capture.release()
cv2.destroyAllWindows()
