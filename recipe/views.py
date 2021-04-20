from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView,ListView
from django.db.models import Q
from .models import Food


# Create your views here.
def home(request):
    return render(request,'home.html')

from django.shortcuts import render
from recipe.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,'recipe/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return render(request,'recipe/index.html')
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
           
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        
    return render(request,'recipe/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'recipe/index.html')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'recipe/login.html', {})

def main(request):
    return render(request,'maincourse.html')

def main1(request):
    return render(request,'main1.html')

def main2(request):
    return render(request,'main2.html')

def main3(request):
    return render(request,'main3.html')

def main4(request):
    return render(request,'main4.html')

def main5(request):
    return render(request,'main5.html')    

def main6(request):
    return render(request,'main6.html')

def main7(request):
    return render(request,'main7.html')

def main8(request):
    return render(request,'main8.html')

def kitchenhacks(request):
    return render(request,'kitchenhacks.html')

def desserts(request):
    return render(request,'desserts.html')

def dessert1(request):
    return render(request,'dessert1.html')

def dessert2(request):
    return render(request,'dessert2.html')

def dessert3(request):
    return render(request,'dessert3.html')

def dessert4(request):
    return render(request,'dessert4.html')

def dessert5(request):
    return render(request,'dessert5.html')

def dessert6(request):
    return render(request,'dessert6.html')

def dessert7(request):
    return render(request,'dessert7.html')

def dessert8(request):
    return render(request,'dessert8.html')



def starters(request):
    return render(request,'starters.html')

def beverages(request):
    return render(request,'beverages.html')

def drink1(request):
    return render(request,'drink1.html')

def drink2(request):
    return render(request,'drink2.html')

def drink3(request):
    return render(request,'drink3.html')

def drink4(request):
    return render(request,'drink4.html')

def drink5(request):
    return render(request,'drink5.html')

def drink6(request):
    return render(request,'drink6.html')

def drink7(request):
    return render(request,'drink7.html')

def drink8(request):
    return render(request,'drink8.html')

def starter1(request):
    return render(request,'starter1.html')

def starter2(request):
    return render(request,'starter2.html')

def starter3(request):
    return render(request,'starter3.html')

def starter4(request):
    return render(request,'starter4.html')

def starter5(request):
        return render(request,'starter5.html')

def starter6(request):
    return render(request,'starter6.html')

def starter7(request):
    return render(request,'starter7.html')

def starter8(request):
    return render(request,'starter8.html')

class SearchResultsView(ListView):
    model = Food
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Food.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
        return object_list