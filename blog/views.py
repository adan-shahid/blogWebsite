from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def index(request):
    return render(request, "blog/index.html")

def	post_detail(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, "blog/post-detail.html", context)
    
