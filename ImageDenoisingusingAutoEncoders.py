# practical experimentation of analyticsvidhya.com/blog/2021/07/image-denoising-using-autoencoders-a-beginners-guide-to-deep-learning-project/

import numpy 
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
import sys
sys.setdefaultencoding('utf-8')
import locale
print(locale.getpreferredencoding())


(X_train, y_train), (X_test, y_test) = mnist.load_data()

