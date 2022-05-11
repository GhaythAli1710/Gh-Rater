from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.utils import json

from myapp.models import Meal, Rating, UploadImageTest, imageupload
from myapp.serializers import MealSerializer, RatingSerializer, ImageSerializer, imageuploadSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ImageViewSet(ListAPIView):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = UploadImageTest.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


class Imageuploadviewset(viewsets.ModelViewSet):
    queryset = imageupload.objects.all()
    serializer_class = imageuploadSerializer
