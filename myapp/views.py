from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets
from myapp.models import Meal, Rating
from myapp.serializers import MealSerializer, RatingSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
