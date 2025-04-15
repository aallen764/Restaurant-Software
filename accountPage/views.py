from django.shortcuts import render, redirect
from signUp.models import user_Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        if request.GET.get('edit') == 'true':
            return render(request, 'accountPage/index.html', {
                'template_data': {'title': 'account'},
                'form': True,  # show the form to change user fields
            })
        else:
            return render(request, 'accountPage/index.html', {
                'template_data': {'title': 'account'},
                'form': False, # close or DON't show form to change user fields
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
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            request.session['update_messages'] = ["Passwords do not match."]
            return redirect('account.index')

        request.user.password = make_password(new_password)
        request.user.save()
        request.session['update_messages'] = ["Password updated successfully."]
        return redirect('account.index')

    return redirect('account.index')

def change_password_page(request):
    if not request.user.is_authenticated:
        return redirect('/')

    return render(request, 'accountPage/change_password.html')
