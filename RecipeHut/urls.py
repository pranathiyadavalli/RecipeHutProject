"""RecipeHut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('recipe.urls')),
    path('special/',views.special,name='special'),
    path('recipe/',include('recipe.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('maincourse/',include('recipe.urls')),
    path('maincourse/main1',include('recipe.urls')),
    path('maincourse/main2',include('recipe.urls')),
    path('maincourse/main3',include('recipe.urls')),
    path('maincourse/main4',include('recipe.urls')),
    path('maincourse/main5',include('recipe.urls')),
    path('maincourse/main6',include('recipe.urls')),
    path('maincourse/main7',include('recipe.urls')),
    path('maincourse/main8',include('recipe.urls')),
    path('kitchenhacks/',include('recipe.urls')),
    path('desserts/',include('recipe.urls')),
    path('desserts/dessert1',include('recipe.urls')),
    path('starters/',include('recipe.urls')),
    path('beverages/',include('recipe.urls')),
    path('beverages/drink1',include('recipe.urls')),
    path('beverages/drink2',include('recipe.urls')),
    path('beverages/drink3',include('recipe.urls')),
    path('beverages/drink4',include('recipe.urls')),
    path('beverages/drink5',include('recipe.urls')),
    path('beverages/drink6',include('recipe.urls')),
    path('beverages/drink7',include('recipe.urls')),
    path('beverages/drink8',include('recipe.urls')),

    path('starters/starter1',include('recipe.urls')),
    path('starters/starter2',include('recipe.urls')),
    path('starters/starter3',include('recipe.urls')),
    path('starters/starter4',include('recipe.urls')),
    path('starters/starter5',include('recipe.urls')),
    path('starters/starter6',include('recipe.urls')),
    path('starters/starter7',include('recipe.urls')),
    path('starters/starter8',include('recipe.urls')),
    
]
