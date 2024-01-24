from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def redirect_to_default_profile(request):
    default_username = request.user.username
    if default_username:
        return redirect('view_profile', username=default_username)
    else:
        # Handle the case where the user has no username
        return render(request, 'login/login.html')


@login_required
def view_profile(request):
    context = {}
    return render(request, 'users/profile.html', context)


def user_profile(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)
    context = {
        'user': user_profile,
    }
    return render(request, 'users/profile.html', context)
