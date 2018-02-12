from __future__ import print_function
from django.http import HttpResponse
import json
import os, io, PIL
from PIL import Image
import cv2
import numpy
# from keras.models import load_model
from keras import models
# import logging
from keras import backend as K
from keras.models import load_model
from scipy.misc import imsave, imread, imresize
from .forms import UploadFileForm
import logging
import win_unicode_console

def index(request):
    # model = load_model('C:\\Users\\james\\PycharmProjects\\karas-test\\my_model.h5')
    # get image out  of request object
    # image = Image.open(io.BytesIO(request.body))
    # cv2.imshow('ImageWindow', image)
    # cv2.waitKey()
    with open('C:\\Users\\james\\Desktop\\drawing2.txt', 'wb+') as destination:
        destination.write(request.read())
    print(request.content_type)
    print(request.encoding)
    print(request.method)
    print(request.POST)
    return HttpResponse(1)

    # x = imread('C:\\Users\\james\\Desktop\\drawing1.png', mode='L')
    # x = numpy.invert(x)
    # x = imresize(x, 28, 28)

    # im = imread("C:\\Users\\james\\PycharmProjects\\karas-test\\5.png")
    #
    # im = im/255
    # im = numpy.expand_dims(im, axis=0)
    # im = numpy.expand_dims(im, axis=0)
    # probs = model.predict(x.reshape(1, 28, 28, 1), 1)
    # prediction = probs.argmax(axis=-1)
    # print(prediction)
    # K.clear_session()
    # return HttpResponse(prediction)