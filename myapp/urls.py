from django.urls import path
from rest_framework import routers
from myapp.views import MealViewSet, RatingViewSet
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('meals', MealViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
