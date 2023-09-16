# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request,'blog/index.html')

def about(request):
    return render(request,'blog/about.html')

def blog(request):
    return render(request,'blog/blog.html')

def features(request):
    return render(request,'blog/features.html')

def contact(request):
    return render(request,'blog/contact.html')

def post_list(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
