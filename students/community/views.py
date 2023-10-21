from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib import auth
from django.contrib import messages
from . import models
# Create your views here.
def login(request):
    messages.error(request, '')
    if request.method == 'POST':
        username = request.POST.get('email')
        
        password = request.POST.get('password')
        
        if username and password:
            
            user = authenticate(request, username=username, password=password )
            if user is not None:
                auth_login(request,user)
                return redirect('home',pk = "-0")
            else:
                messages.error(request, 'username or password not correct.')
                
    return render(request, 'login/login.html')
def logout(request):
    user = request.user
    if user.is_superuser:
        auth.logout(request)
        return redirect('admin_control:admin_login')
    auth.logout(request)
    return redirect('login:login')
def home(request,pk):
    
    user = request.user
    filtered_data = models.postUser.objects.filter(creator=user)
    filtered_post = models.Discussion.objects.filter(writers=user).exclude(thread__creator=user)
    discussions = models.Discussion.objects.filter(thread__threads=pk)
    for i in discussions:
        print(i.comments)
    dic = {"thread": filtered_data, 'comments':filtered_post, "disc":discussions}
    return render(request, 'homes/home.html',dic)
