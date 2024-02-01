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
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        no_of_logins = profile.no_of_logins
    except Profile.DoesNotExist:
        profile = None
        no_of_logins = 0
    context = {
        'no_of_logins': no_of_logins
    }
    if request.method == 'POST':
        image = request.FILES.get('profile-image')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        if no_of_logins == 0:
            if image and first_name and last_name and email:
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()

                profile = Profile.objects.create(user=user, image=image, no_of_logins=1)
                messages.success(request, 'Profile created successfully!')
                return redirect('user_profile', username=user.username)
            else:
                messages.error(request, 'Please fill all fields.')
                return redirect('create_profile')
        else:
            if image:
                profile.image = image

            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if email:
                user.email = email

            user.save()
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_profile', username=user.username)

    return render(request, 'users/create_profile.html', context)
