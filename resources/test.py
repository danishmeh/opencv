import cv2 as cv
import dlib

# Load the face detector and create the face recognition model
detector = dlib.get_frontal_face_detector()
face_recognizer = dlib.face_recognition_model_v1("path/to/your/dlib_face_recognition_model.dat")

# Mapping of recognized person encodings to their names
person_encodings = {
    # Add the encodings and corresponding names of recognized individuals
}

# Define the video capture source (0 for default webcam)
video_source = 0

# Define the output video file name
output_file = "output.avi"

# Set up video capture
cap = cv.VideoCapture(video_source)

# Get the default video capture width and height
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create a VideoWriter object
fourcc = cv.VideoWriter_fourcc(*"XVID")  # Use appropriate codec (e.g., "XVID", "mp4v", etc.)
out = cv.VideoWriter(output_file, fourcc, 20.0, (frame_width, frame_height))

# Start the video capture loop
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    # Process each detected face
    for face in faces:
        # Obtain the face encodings
        face_encodings = face_recognizer.compute_face_descriptor(frame, face)

        # Compare with known person encodings
        for name, known_encoding in person_encodings.items():
            # Calculate the Euclidean distance between face encodings
            distance = dlib.distance(face_encodings, known_encoding)

            # Set a distance threshold for recognition
            if distance < 0.6:  # Adjust this value for better recognition accuracy
                # Overlay the name on the frame
                cv.putText(frame, name, (face.left(), face.top() - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Write the frame to the output video file
    out.write(frame)

    # Display the live video stream
    cv.imshow("Webcam", frame)

    # Check for 'q' key press to stop the video capture loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and video writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv.destroyAllWindows()
