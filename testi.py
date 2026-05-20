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
    
    # Check for key presses
    key = cv2.waitKey(1) & 0xFF
    if key != 255:
        print(f"Key pressed: {key}")

    # Press 'q' to exit and save a photo
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite('photo.jpg', frame)
        print("Saved photo.jpg")

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()