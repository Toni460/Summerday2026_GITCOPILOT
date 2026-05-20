import cv2

# Access the default camera (0 is the default index)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Apply a simple filter (grayscale)
    filtered_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the filtered frame
    cv2.imshow('Laptop Camera', filtered_frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()