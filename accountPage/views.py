from django.shortcuts import render, redirect
from signUp.models import user_Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import login, authenticate


def index(request):
    if request.user.is_authenticated:
        #request.session['update_messages'] = ["Password updated successfully."]
        if request.GET.get('edit') == 'true':
            return render(request, 'accountPage/index.html', {
                'template_data': {'title': 'account'},
                'form': True,  # show the form to change user fields
            })
        else:
            return render(request, 'accountPage/index.html', {
                'template_data': {'title': 'account'},
                'form': False, # close or DON'T show form to change user fields
            })
    else:
        return redirect('/')

def update_account(request):
    if request.method == 'POST':
        user = request.user
        profile = user.user_profile

        # update username (default user field)
        user.username = request.POST.get('username', user.username)
        user.save()

        # update user info with new inputted fields (custom fields)
        profile.zip_code = request.POST.get('zip_code', profile.zip_code)
        profile.email_address = request.POST.get('email_address', profile.email_address)
        profile.phone_number = request.POST.get('phone_number', profile.phone_number)
        profile.save()

        return redirect('account.index') # send back to account page when done editing

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

        request.user.set_password(new_password)
        request.user.save()
        login(request, user)
        request.session.pop('update_messages', None)
        request.session['update_messages'] = ["Password updated successfully."]
        return render(request, 'accountPage/index.html')
    #request.session.pop('update_messages', None)
    return render(request, 'accountPage/change_password.html')