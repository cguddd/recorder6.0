# trips/views.py

from datetime import datetime
#from flask import request
from django.shortcuts import render, redirect
from trips.forms import DocumentForm
from django.db import models
from trips.models import Document
from django.http import HttpResponse
from django.utils.html import escape
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from django.template.loader import get_template
from django import template
from django.shortcuts import render

from label_wav import label_wav
import datetime
import json
from pydub import AudioSegment

framerate=16000
wav_add='documents/theRecog.wav'

ctx = {}
rlt = ""
#words = ['一','二','三','四','五','六','七','八','九','十','後退','前進','上','下','左','右','床','去','快樂','房屋','樹','鳥','貓','狗','志明','春嬌','可以','不可','開','關']
#ctx['th'] = 0
word = ""
ctx['word'] = "一"

def main(request):
    return render(request, 'main.html', {})

def recognizer(request):
    return render(request, 'recognizer.html', {})

def recorder(request):
    return render(request, 'recorder.html', {})

def set_name(request):
    return render(request, 'set_name.html', {})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/upload')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

def upload_word(request):
    ctx['word'] = request.POST.get('thisword')
    return HttpResponse(escape(repr(request)))

def upload(request):
    customHeader = request.META['HTTP_MYCUSTOMHEADER']

    time = "documents/" + ctx['word']  + "/" + ctx['word']  + "_" + ctx['rlt'] + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")[:-3] + ".wav"
    # obviously handle correct naming of the file and place it somewhere like media/uploads/
    uploadedFile = open(time, "wb")
    # the actual file is in request.body
    uploadedFile.write(request.body)
    uploadedFile.close()
    # put additional logic like creating a model instance or something like this here
    return HttpResponse(escape(repr(request)))

def name_post(request):
    if request.POST:
        ctx['rlt'] = request.POST['q']
        if(ctx['rlt'] == ""):
            ctx['rlt'] = "user" + datetime.datetime.now().strftime("%f")[:-3]
        return render(request, "recorder.html", ctx)
    else:
        ctx['rlt'] = ""
        return render(request, "set_name.html")

def model_form_uploadRecog(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()          
        return redirect('/uploadRecog')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

###the recog file to create

def uploadRecog(request):
    
    customHeader = request.META['HTTP_MYCUSTOMHEADER']
    # nowTime=datetime.datetime.now().strftime("%Y%m%d_%H%M%S") 
    time = "documents/theRecog.wav"
    # obviously handle correct naming of the file and place it somewhere like media/uploads/
    uploadedFile = open(time, "wb")
    # the actual file is in request.body
    uploadedFile.write(request.body)
    print("this recog")
    uploadedFile.close()


    
    return render(request,'recorder.html',)

def  recog(request):
    
    sound = AudioSegment.from_wav("documents/theRecog.wav")
    sound=sound.set_frame_rate(16000)
    sound.export("documents/theNewRecog.wav", format="wav")
    result=label_wav(wav='documents/theNewRecog.wav',
                graph='my_frozen_graph.pb',
                labels='conv_labels.txt',
                input_name='wav_data:0',
                output_name='labels_softmax:0',
                how_many_labels=3,
                        )

    notResult = ",".join(result)
    strResult="\""+notResult+"\""
    print(strResult)
    return HttpResponse(strResult)