from django.shortcuts import render, redirect
from signUp.models import user_Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import login, authenticate

# ✅ NEW import for handling the form
from .forms import ProfileUpdateForm


def index(request):
    if request.user.is_authenticated:
        if request.GET.get('edit') == 'true':
            return render(request, 'accountPage/index.html', {
                'template_data': {'title': 'account'},
                'form': True,
            })
        else:
            return render(request, 'accountPage/index.html', {
                'template_data': {'title': 'account'},
                'form': False,
            })
    else:
        return redirect('/')


def update_account(request):
    if request.method == 'POST':
        user = request.user
        profile = user.user_profile

        # ✅ Use the ModelForm to update both text fields and the profile picture
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Update username separately since it's on the User model
            user.username = request.POST.get('username', user.username)
            user.save()
            form.save()
        return redirect('account.index')

    return redirect('account.index')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('/')
        
    if request.method == 'POST':
        user = request.user
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            request.session['update_messages'] = ["Passwords do not match."]
            return render(request, 'accountPage/change_password.html')

        user.set_password(new_password)
        user.save()
        login(request, user)
        request.session['update_messages'] = ["Password updated successfully."]
        return render(request, 'accountPage/index.html')

    return render(request, 'accountPage/change_password.html')
