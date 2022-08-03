from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api_img', views.api_imgview, basename="testapi")
urlpatterns = [
    path('',include(router.urls)),
    path('viewinput/<str:input_id>', views.viewInput, name='viewinput'),
    path('editImage', views.editImage, name='editImage'),
]
