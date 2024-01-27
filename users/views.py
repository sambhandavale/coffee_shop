from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def redirect_to_default_profile(request):
    default_username = request.user.username
    if default_username:
        return redirect('user_profile', username=default_username)
    else:
        return render(request, 'login/login.html')


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return redirect('create_profile')
    return render(request, 'users/profile.html', {'user': profile})


def create_profile(request):
    if request.method == 'POST':
        user = request.user
        if 'profile-image' in request.FILES:
            image = request.FILES['profile-image']
            profile = Profile(user=user, image=image)
            profile.save()
        else:
            messages.error(request, 'Please upload a profile image.')
            return redirect('create_profile')

        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request, 'Profile created successfully!')
        return redirect('user_profile', username=user.username)

    return render(request, 'users/create_profile.html')
