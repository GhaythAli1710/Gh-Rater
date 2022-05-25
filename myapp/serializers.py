from django.contrib.auth.models import User
from rest_framework import serializers, validators

from myapp.models import Meal, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'email': {
                'required': True,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), f'Email already exists'
                    )
                ]
            },
            'password': {'write_only': True, 'required': True}
        }


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description', 'no_of_ratings', 'avg_ratings']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'meal', 'stars']
# uuid vs id
