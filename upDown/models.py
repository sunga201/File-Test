from django.db import models
from .common import file_upload_path
# Create your models here.
class FileTest(models.Model):
    id=models.AutoField(primary_key=True)
    path=models.FileField(upload_to=file_upload_path, null=True)