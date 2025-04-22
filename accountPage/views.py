from django.shortcuts import render, redirect
from signUp.models import user_Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate


def index(request):
    if request.user.is_authenticated:
        update_messages = request.session.pop('update_messages', [])

        if request.GET.get('edit') == 'true':
            return render(request, 'accountPage/index.html', {
                'template_data': {'title': 'account'},
                'form': True,
                'update_messages': update_messages
            })
        else:
            return render(request, 'accountPage/index.html', {
                'template_data': {'title': 'account'},
                'form': False,
                'update_messages': update_messages
            })
    else:
        return redirect('/')

def update_account(request):
    if request.method == 'POST':
        user = request.user
        profile = user.user_profile

        # update userfields with newly inputted info
        new_username = request.POST.get('username', user.username)
        new_zip = request.POST.get('zip_code', profile.zip_code)
        new_email = request.POST.get('email_address', profile.email_address)
        new_phone = request.POST.get('phone_number', profile.phone_number)
        
        # list to hold/catch any errors that come from new profile info
        errors = []
        
        # check if unique fields are TRULY unique --> if not, append an error to list
        if User.objects.filter(username=new_username).exclude(id=user.id).exists():
            errors.append("Username is already taken.")
        if user_Profile.objects.filter(email_address=new_email).exclude(user=user).exists():
            errors.append("Email address is already in use.")
        if new_phone and user_Profile.objects.filter(phone_number=new_phone).exclude(user=user).exists():
            errors.append("Phone number is already in use.")

        # if any errors were caught, we send them to the html as a session and update the page
        if errors:
            request.session['update_messages'] = errors
            return redirect('account.index')
        
        # save new user info if NO ERRORS were caught
        user.username = new_username
        user.save()
        profile.zip_code = new_zip
        profile.email_address = new_email
        profile.phone_number = new_phone
        profile.save()

        request.session['update_messages'] = ["Account information updated successfully."]
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
        
        request.session['update_messages'] = ["Password updated successfully."]
        return redirect('account.index')

    return render(request, 'accountPage/change_password.html')