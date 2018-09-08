from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models

"""
class 影音檔案欄位(models.Model):
    影音 = models.FileField(blank=True)
    語言 = models.CharField(blank=True, max_length=50)
    測試 = models.CharField(blank=True, max_length=50)
"""

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='Wav_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)