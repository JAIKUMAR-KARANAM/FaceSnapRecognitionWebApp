import face_recognition
import os

def face_recognition_optimized(reference_path, target_path, tolerance=0.6):
    reference_image = face_recognition.load_image_file(reference_path)
    reference_face_encoding = face_recognition.face_encodings(reference_image)[0]

    images_path = []

    # Use a faster face detection model (hog)
    for filename in os.listdir(target_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            target_image_path = os.path.join(target_path, filename)

            # Encoding the Image Faces
            target_image = face_recognition.load_image_file(target_image_path)
            target_face_encodings = face_recognition.face_encodings(target_image, model="small")

            if target_face_encodings:
                # Face Comparison is Started
                result = face_recognition.compare_faces([reference_face_encoding], target_face_encodings[0], tolerance=tolerance)

                if result[0]:
                    print("It's a picture of me!", target_image_path)
                    images_path.append(target_image_path)
                else:
                    print("It's not a picture of me!", target_image_path)

    return images_path

if __name__ == "__main__":
    reference_image_path = "C:\\Users\\User\\Desktop\\target\\IMG20230928120934.jpg"
    target_images_path = "C:\\Users\\User\\Desktop\\target"
    result_images = face_recognition_optimized(reference_image_path, target_images_path, tolerance=0.5)
    print("Result Images:", result_images)
