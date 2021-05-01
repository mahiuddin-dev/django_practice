from django.shortcuts import render

from .models import UserProfile

# Create your views here.

def homepage(request):
    userInfo = UserProfile.objects.all()
    userData = {'userInfo': userInfo}
    return render(request,'index.html',userData)

