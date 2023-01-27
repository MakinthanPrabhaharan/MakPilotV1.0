868484848484848# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:23:20 2020

@author: padch
"""

import tensorflow as tf
import numpy as np
import cv2
from PIL import ImageGrab
import time

from Truck import Truck

#path to model
model_directory = 'truckdrivemodelV3.h5'


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#loading in trained model
model = tf.keras.models.load_model(model_directory)

print('MakPilot Version 1.0')

time.sleep(1)

actros = Truck()

#accelerating forward for two seconds
actros.forward(2)

print('***MakPilot Engaged***')


while True:
    image = ImageGrab.grab(bbox = (572, 340, 572 + 230, 340 + 120))

    image = np.array(image)

    image = cv2.resize(image, (184,96))
    
    image2 = np.reshape(image , (-1,96,184,3))
    
    image2 = tf.cast(image2, tf.float32)
    
    prediction = model.predict([image2]).round()
    
    turnidx = np.argmax(prediction)
    
    if turnidx == 0:
        actros.forward(0)
    elif turnidx == 1:
        actros.left(0.074)
    elif turnidx ==2:
        actros.right(0.074)
    
    print(turnidx)
