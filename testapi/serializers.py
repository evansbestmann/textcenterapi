from rest_framework import serializers
from .models import *
from PIL import Image
from PIL import ImageDraw


class api_imgSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = api_img
        fields  = ('id','title','images')
        depth = 1