from django.shortcuts import render, redirect
from signUp.models import user_Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user
    profile = user.user_profile

    if request.method == 'POST':
        username = request.POST.get('username', user.username)
        zip_code = request.POST.get('zip_code', profile.zip_code)
        email_address = request.POST.get('email_address', profile.email_address)
        phone_number = request.POST.get('phone_number', profile.phone_number)

        user.username = username
        user.save()

        profile.zip_code = zip_code
        profile.email_address = email_address
        profile.phone_number = phone_number
        profile.save()

        return redirect('account.index') # safe case

    return render(request, 'accountPage/index.html', {
        'user': user,
        'user_profile': profile,
        'template_data': {'title': 'account'}
    })

@login_required
def update_account(request):
    if request.method == 'POST':
        user = request.user
        profile = user.user_profile

        user.username = request.POST.get('username', user.username)
        user.save()

        profile.zip_code = request.POST.get('zip_code', profile.zip_code)
        profile.email_address = request.POST.get('email_address', profile.email_address)
        profile.phone_number = request.POST.get('phone_number', profile.phone_number)
        profile.save()

        return redirect('account.index')
    
    return redirect('account.index')  #safe case
