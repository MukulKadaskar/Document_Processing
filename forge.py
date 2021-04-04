import numpy as np
from PIL import Image, ImageChops, ImageEnhance
import os
import itertools
import shutil
from imageio import imread
import imageio
import pandas as pd
import cv2
import tensorflow as tf
import keras

def generate_ela(path,quality):
  temp_file = 'temp_file.jpg'
  # ela_filename = 'temp_ela.png'
  
  image = Image.open(path).convert('RGB')
  image.save(temp_file, 'JPEG', quality = quality)
  temp_image = Image.open(temp_file)
  
  ela_img = ImageChops.difference(image, temp_image)
  
  extrema = ela_img.getextrema()
  max_diff = max([ex[1] for ex in extrema])
  if max_diff == 0:
      max_diff = 1
  scale = 255.0 / max_diff
  
  ela_img = ImageEnhance.Brightness(ela_img).enhance(scale)
  
  return ela_img

def get_image(path):
    return np.array(generate_ela(path, 90).resize((128,128))).flatten()/255

def forge(img):
    model = keras.models.load_model('model_data/forge.h5')
    X_test = []
    X_test.append(get_image('uploads/'+img))
    X_test = np.array(X_test)
    X_test = X_test.reshape(-1, 128, 128, 3)
    Y_pred_test = model.predict(X_test)
    Y_pred_classes_test = np.argmax(Y_pred_test,axis = 1)
    # print(Y_pred_classes_test)
    pred = int(Y_pred_classes_test)
    return pred

if __name__=='__main__':
    forge('prathamesh.jpg')