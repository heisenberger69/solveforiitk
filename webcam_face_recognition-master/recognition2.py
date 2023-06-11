import dlib
import cv2

# Load the pre-trained face recognition model
face_rec_model = dlib.face_recognition_model_v1('path_to_model.dat')

# Load the image for face recognition
image = cv2.imread('path_to_image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
face_detector = dlib.get_frontal_face_detector()
faces = face_detector(gray_image)

# Load the face landmarks model
shape_predictor = dlib.shape_predictor('path_to_shape_predictor.dat')

# Iterate over detected faces
for face in faces:
    # Get the face landmarks
    landmarks = shape_predictor(gray_image, face)
    
    # Compute the face descriptor
    face_descriptor = face_rec_model.compute_face_descriptor(gray_image, landmarks)
    
    # Perform face recognition here, such as comparing the descriptor to a known database of face descriptors
    
    # Example: Print the computed face descriptor
    print(face_descriptor)

# Display the image with rectangles around the detected faces
for face in faces:
    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

cv2.imshow('Face Recognition', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
