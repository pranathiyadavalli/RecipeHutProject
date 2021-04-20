from django.contrib import admin
from recipe.models import UserProfileInfo, User
from .models import Food

# Register your models here.
admin.site.register(UserProfileInfo)

class FoodAdmin(admin.ModelAdmin):
    list_display = ("name","category",)

admin.site.register(Food,FoodAdmin)
