from django.contrib import admin
from .models import Meal, Rating, UploadImageTest


# Register your models here.
class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'meal', 'stars']
    list_filter = ['user', 'meal']


admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(UploadImageTest)
