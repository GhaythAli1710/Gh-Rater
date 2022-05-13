from rest_framework import viewsets, generics
from myapp.models import Meal, Rating, Ghayth
from myapp.serializers import MealSerializer, RatingSerializer, GhSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class GhImage(generics.ListCreateAPIView):
    queryset = Ghayth.objects.all()
    serializer_class = GhSerializer
    # b = base64.b64decode(request.data['image'])
    # print(b)
