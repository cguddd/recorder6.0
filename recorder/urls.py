"""recorder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include, url
from trips.views import recorder, model_form_upload, upload, name_post, set_name, upload_word, model_form_uploadRecog,uploadRecog,recog,recognizer,main,upload_file,self_recorder,self_name_post

urlpatterns = {
    path('admin/', admin.site.urls),
    path('recorder_origin', recorder),
    path('upload', model_form_upload),
    path('upload_server', upload), 
    path('recorder', name_post), #or main
    path('set_name', set_name),
    path('upload_word', upload_word),
    path('uploadRecog', model_form_upload),
    path('uploadRecog_server', uploadRecog),
    path('recogResult', recog),
    path('recognizer', recognizer),
    path('upload_file',upload_file),
    path('self_recorder',self_name_post),
    path('',main),
}
