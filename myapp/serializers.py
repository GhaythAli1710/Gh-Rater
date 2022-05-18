from rest_framework import serializers

from myapp.models import Meal, Rating


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description', 'no_of_ratings', 'avg_ratings']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'meal', 'stars']
# uuid vs id
