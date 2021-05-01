from django.shortcuts import render
from .models import Blogpost
# Create your views here.

def index(request):
    allpost = Blogpost.objects.all()
    return render(request,'Blog/index.html', {'allpost': allpost})

def blogpost(request,post_id):
    vPost = Blogpost.objects.filter(PosttId = post_id)
    return render(request,'Blog/blogpost.html', {'vPost': vPost[0]})