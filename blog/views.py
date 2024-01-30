from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages


def blog(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'blog/blogs.html', context)


def write_review(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        Post.objects.create(content=review, author=request.user)
        messages.success(request, f'Review Added by {request.user.username}')
        return redirect('blog-home')
