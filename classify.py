import os
# os.environ["CUDA_VISIBLE_DEVICES"]="-1" 
import tensorflow as tf
import keras
import cv2
import numpy as np
import os
import tensorflow as tf



def classify(img):
    model = keras.models.load_model('model_data/vggtrained_model.h5')
    img = cv2.imread('uploads/'+img, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224))
    img = np.array(img)
    x = np.expand_dims(img, axis=0)
    classes = np.argmax(model.predict(x), axis=-1)
    res = int(classes)
    # print(res)
    return res

if __name__=='__main__':
    print(tf.__version__)
    classify('uploads/upload.png')