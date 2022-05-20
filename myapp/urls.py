from django.urls import path
from rest_framework import routers
from myapp.views import MealViewSet, RatingViewSet, UserViewSet
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('meals', MealViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
