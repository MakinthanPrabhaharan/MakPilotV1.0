# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:40:19 2020

@author: padch
"""

#importing the pressKey, releaseKey and up, down , left, right methods and variables from the KeySender class
from KeySender import pressKey, releaseKey, up, down, left, right
import time

class Truck:
    
    def left(self, duration):
        pressKey(left)
        #pressKey(up)
        time.sleep(duration)
        releaseKey(left)
        #releaseKey(up)
        #time.sleep(0.05)
    def right(self, duration):
        pressKey(right)
        #pressKey(up)
        time.sleep(duration)
        releaseKey(right)
        #releaseKey(up)
        #time.sleep(0.05)
        
    def forward(self, duration):
        #pressKey(up)
        time.sleep(duration)
        #releaseKey(up)