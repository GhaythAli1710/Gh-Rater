from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from myapp.models import Meal, Rating
from myapp.serializers import MealSerializer, RatingSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=['POST'], detail=True)
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update
            '''
            username = request.data['username']
            user = User.objects.get(username=username)
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            try:
                # update
                rating = Rating.objects.get(user=user.id, meal=meal.id)  # meal.id or pk
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                jason = {
                    'message': 'Meal rate updated',
                    'result': serializer.data
                }
                return Response(jason, status=status.HTTP_200_OK)
            except:
                # create
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                jason = {
                    'message': 'Meal rate created',
                    'result': serializer.data
                }
                return Response(jason, status=status.HTTP_200_OK)
        else:
            '''
            send message 
            '''
            json = {
                'message': 'stars not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
