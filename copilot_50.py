import cv2
import numpy as np

# Apply a 1950s-style sepia and vignette effect for saved photos
def apply_50s_style(image):
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    styled = cv2.transform(image, sepia_filter)
    styled = np.clip(styled, 0, 255).astype('uint8')

    rows, cols = styled.shape[:2]
    kernel_x = cv2.getGaussianKernel(cols, cols / 2)
    kernel_y = cv2.getGaussianKernel(rows, rows / 2)
    kernel = kernel_y * kernel_x.T
    mask = kernel / np.max(kernel)
    for i in range(3):
        styled[:, :, i] = styled[:, :, i] * mask

    return styled

# Overlay poster-style text onto an image
def overlay_poster_text(image, text="SUMMERDAY 2026", position=(30, 60), color=(0, 165, 255), thickness=3):
    font = cv2.FONT_HERSHEY_TRIPLEX
    scale = 2
    shadow_color = (0, 0, 0)
    x, y = position
    cv2.putText(image, text, (x + 2, y + 2), font, scale, shadow_color, thickness + 2, cv2.LINE_AA)
    cv2.putText(image, text, position, font, scale, color, thickness, cv2.LINE_AA)
    return image

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

    # Display the poster-style frame with text
    display_frame = frame.copy()
    overlay_poster_text(display_frame)
    cv2.imshow('Laptop Camera', apply_50s_style(display_frame))

    # Check for key presses
    key = cv2.waitKey(1) & 0xFF
    if key != 255:
        print(f"Key pressed: {key}")

    # Press 'q' to exit and save a photo
    if key == ord('q'):
        break
    elif key == ord('s'):
        styled_photo = apply_50s_style(frame)
        overlay_poster_text(styled_photo, "SUMMERDAY 2026", (30, 60), (0, 255, 255), 3)
        cv2.imwrite('photo.jpg', styled_photo)
        print("Saved photo.jpg with 50s style and poster text")


# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()