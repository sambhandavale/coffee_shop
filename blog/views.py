from django.shortcuts import render
from .models import Post

def blog(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'blog/blogs.html',context)
