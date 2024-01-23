from django.shortcuts import render, get_object_or_404
from .models import Profile


def view_profile(request):
        context = {}
        return render(request, 'users/profile.html', context)


def user_profile(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)
    context = {
        'user': user_profile,
    }
    return render(request, 'users/profile.html', context)

