
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import api_img
from rest_framework import viewsets
from .serializers import api_imgSerializer
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

# Create your views here.
class api_imgview(viewsets.ModelViewSet):
    queryset = api_img.objects.all()
    serializer_class = api_imgSerializer

def viewInput(request,input_id):
    queryset = api_img.objects.get(id=input_id)
    return render(request,'testapi/viewinput.html',{"queryset":queryset,"id":input_id})

def editImage(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        input_id = request.POST.get("input_id")
        image = api_img.objects.get(id=input_id).images
        title = api_img.objects.get(id=input_id).title
        width = api_img.objects.get(id=input_id).width
        height = api_img.objects.get(id=input_id).height
        try:
            canvas = Image.open(image)
            temp_file = ImageDraw.Draw(canvas)
            temp_file.text((250, 200), title, fill=('black'))
            blob = BytesIO()
            canvas.save(blob, 'JPEG')
            newImage_model = api_img.objects.get(id=input_id)
            newImage_model.images.save(f'{title}.jpg', File(blob), save=True)
            return HttpResponseRedirect(reverse("viewinput", kwargs={"input_id": input_id}))
        except:
           return HttpResponseRedirect(reverse("/"))



