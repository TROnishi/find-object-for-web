# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import ImageModels
from .forms import ImageForm
import params
import detection_mod
import cv2
from PIL import Image
import random

def save_image(img):
    name = random.randint(0,1000000)
    save_path = '{0}{1}.png'.format(params.image_save_path, str(name))
    print('save:'+save_path)
    img.save(save_path)
    return params.original_path+str(name)+".png"

def index(request):

    if request.method == 'GET':
        param = {
            'title':'画像を送ってね',
            'msg':'画像が入ってなかったよ',
        }
        return render(request, 'form.html',{
            'form':ImageForm(),
        })
    elif request.method == 'POST':
        SSD = detection_mod.Detection()
        img = Image.open(request.FILES['image'])
        original_path = save_image(img)
        res_img, result_path = SSD.detection(img)
        
        param = {
            'original_path':original_path,
            'result_path':result_path,
        }
        return render(request, 'res_index.html', param)
    # return render(request, 'hello/index.html')