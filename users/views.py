from django.shortcuts import render

def update_profile(request):
    return render(request, 'users/profile-update.html')

def user_login(request):
    return render(request, 'users/login.html')

def user_logout(request):
    return render(request, 'users/logout.html')
