############# Run this file to crop the images and resize them #############
from facenet_pytorch import MTCNN
from PIL import Image
from PIL import Image, ImageOps
import cv2 


mtcnn = MTCNN(image_size=224, margin=20, keep_all=True, post_process=False, device='cuda')

# face detection code, save cropped face 
# https://www.kaggle.com/timesler/guide-to-mtcnn-in-facenet-pytorch
IMAGE_SIZE = 224
print("Images being cropped and resized ... ")
for person in range(1, 51):
    if person == 47: continue
    for idx in range(1, 6):
        # Load a single image and display
        frame = cv2.imread(f'dataset/{person}/TD_RGB_E_{idx}.jpg')
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (IMAGE_SIZE, IMAGE_SIZE))
        frame = Image.fromarray(frame)

        mtcnn(frame, save_path=f'cropped/TD_RGB_E_{person}_{idx}.jpg')
        
print("New Images saved in cropped folder")