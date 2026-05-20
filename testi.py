import cv2

# Access the default camera (0 is the default index)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Apply a simple filter (grayscale)
    filtered_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(filtered_frame, 1.3, 5)
    
    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the filtered frame
    cv2.imshow('Laptop Camera', frame)

    # Display the frame
    #cv2.imshow('Laptop Camera', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite('photo.jpg', frame)
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()