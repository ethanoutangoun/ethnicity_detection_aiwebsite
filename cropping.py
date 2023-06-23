import cv2


#Takes in a face image "face.jpg" and crops it, returning it as "cropped.jpg" in the same directory


# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect and crop the largest face in an image
def crop_largest_face(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        # Find the largest face
        (x, y, w, h) = max(faces, key=lambda f: f[2] * f[3])

        # Crop the largest face region from the original image
        face_crop = image[y:y+h, x:x+w]

        if face_crop is not None:
        # Save the cropped face image
            cv2.imwrite("./uploads/cropped.jpg", face_crop)

      

    else:
        print("No faces detected in the image.")
        return None

# Example usage
"""
input_image_path = "face.jpg"  # Replace with the path to your input image
cropped_face = crop_largest_face(input_image_path)

if cropped_face is not None:
    # Save the cropped face image
    cv2.imwrite("cropped.jpg", cropped_face)
"""