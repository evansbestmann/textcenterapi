from django.db import models
from PIL import Image, ImageDraw
import io
from io import StringIO,BytesIO
from django.core.files import File

class api_img(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    width = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    images = models.ImageField(upload_to="images",null=True, blank=True)




