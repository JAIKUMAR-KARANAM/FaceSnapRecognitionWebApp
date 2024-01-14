import face_recognition
import os
import cv2

target_path = 'C:/Users/User/Desktop/21.8.23/'
reference_path = "C:\\Users\\User\\Desktop\\21.8.23\\_DSC0990.jpg"
def face_recognition_(reference_path,target_path,tolerance=0.6):
    Rimage = cv2.imread(reference_path)
    Rimage = cv2.resize(Rimage, (0, 0), None, 0.25, 0.25)
    Rimage = cv2.cvtColor(Rimage, cv2.COLOR_BGR2RGB)
    faceRimage = face_recognition.face_locations(Rimage)
    reference_face_encoding = face_recognition.face_encodings(Rimage, faceRimage)[0]
    images_path = []
    
    for filename in os.listdir(target_path):
        if filename.endswith(('.JPG', '.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            target_image_path = os.path.join(target_path, filename)
            image = cv2.imread(target_image_path)
            image = cv2.resize(image, (0, 0), None, 0.25, 0.25)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            faceimage = face_recognition.face_locations(image)
            target_face_encodings = face_recognition.face_encodings(image, faceimage)
       
            
            if target_face_encodings:
                # Face Comparison is Started
                results=[]
                for i in range(len(target_face_encodings)):
                    result = face_recognition.compare_faces([reference_face_encoding], target_face_encodings[i], tolerance=tolerance)
                    results.append(result[0])
                print(results)
                if True in results:
                    print("It's a picture of me!", target_image_path)
                    images_path.append(filename)
                else:
                    print("It's not a picture of me!",target_image_path)
    return images_path
if __name__== "__main__":
    print(face_recognition_(reference_path,target_path))