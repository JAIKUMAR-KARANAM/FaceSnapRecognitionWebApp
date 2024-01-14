from face_rec import *
import shutil
import os 

target_path = 'C:\\Users\\User\\Desktop\\21.8.23\\'
reference_path = "C:\\Users\\User\\Desktop\\21.8.23\\_DSC0990.jpg"
def image_retrival(target_path,reference_path,directory_name):
    Selected_Images=face_recognition_(reference_path,target_path)
    print(Selected_Images)
    directory = directory_name
    parent_dir = "D:\\project_j\\static\\images\\prd_images"
    path = os.path.join(parent_dir, directory) 
    os.mkdir(path) 
    print("Directory '% s' created" % directory)

    destination = "D:\\project_j\\static\\images\\prd_images\\"+str(directory_name)
    for f in Selected_Images:
        src_path = os.path.join(target_path, f)
        dst_path = os.path.join(destination, f)
        shutil.copy(src_path, dst_path)
        return 'successfull'
    return 'Failed'
    