from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)

    def avg_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        if len(ratings) > 0:
            sum = 0
            for rate in ratings:
                sum += rate.stars
            return sum / len(ratings)
        else:
            return 0

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.meal.__str__()

    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)


class Ghayth(models.Model):
    string = models.CharField(max_length=300000)
