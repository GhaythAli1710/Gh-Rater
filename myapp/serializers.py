from rest_framework import serializers

from myapp.models import Meal, Rating, UploadImageTest, imageupload


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'meal', 'stars']


# uuid vs id
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ('name', 'image')


class imageuploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = imageupload
        fields = (
            'title',
            'images'
        )
