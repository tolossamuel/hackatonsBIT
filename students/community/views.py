from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib import auth
from django.contrib import messages
from . import models
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def startHome(request):
    return render(request, "homepage/index.html")
def login(request):
    messages.error(request, '')
    if request.method == 'POST':
        username = request.POST.get('email')
        
        password = request.POST.get('password')
        
        if username and password:
            
            user = authenticate(request, username=username, password=password )
            if user is not None:
                auth_login(request,user)
                return redirect('home',pk = "Community")
            else:
                messages.error(request, 'username or password not correct.')
    return render(request, 'login/login.html')
def logout(request):
    
    auth.logout(request)
    return redirect('login')
@login_required(login_url='/login')
def home(request,pk):
    
    user = request.user
    username = user.username[:1]
    about = ""
    filtered_data = models.postUser.objects.filter(creator=user)
    filtered_post = models.Discussion.objects.filter(writers=user).exclude(thread__creator=user)
    discussions = models.Discussion.objects.filter(thread__threads=pk)
    otherThreads = models.other.objects.filter(user = user)
    try:
         about = models.postUser.objects.get(threads=pk)
    except:
        pass
    dic = {"thread": filtered_data, 'comments':filtered_post, "disc":discussions,"pk":pk,"about":about,"user":user,"username":username,"list1":otherThreads}
    
    return render(request, 'homes/home.html',dic)
@login_required(login_url='/login')
def saveComments(request,pk):
    
    user = request.user
    
    if request.method == 'POST':
         image = ''
         comments = request.POST.get('comments')
         try:
              image = request.FILES['image']
         except:
             pass
         if comments or image:
             if not(models.Discussion.objects.filter(writers = user).exists()):                 
                 models.postUser.objects.get(threads = pk).groupMembers += 1
                 models.postUser.objects.get(threads = pk).save()
             thread = models.postUser.objects.get(threads = pk)
             newComments = models.Discussion(thread = thread, comments = comments, writers = user)
             if image:
                  newComments.images = image
             newComments.save() 
    if not(models.other.objects.filter(user = user, name = pk).exists()):
         newOther = models.other(user = user, name = pk)
         newOther.save()
                 
    return redirect('home',pk = pk)
@login_required(login_url='/login')
def search(request,pk):
    if request.GET.get('search') != None :
        search = request.GET.get('search')
        if (models.postUser.objects.filter(threads = search).exists()):
             return redirect("home", pk = search)
    else:
        search = '#'
    
    group = models.postUser.objects.filter(
        Q(threads__icontains = search) 
        )
    patient_count = group.count()
    
    if patient_count == 0:
        return redirect('home',pk=pk)
    dictionary = {'group':group}
    return render(request, "listSearch/index.html",dictionary)
@login_required(login_url='/login')
def createNew(request):
    
    return render(request, "homes/channel.html")
@login_required(login_url='/login')
def supportToCreate(request):
    user = request.user
    print(123)
    if request.method == 'POST':
        now = timezone.now()
        channelName = request.POST.get('channel-name')
        
        description = request.POST.get('channel-description')
        print(123)
        if channelName and description:
            if models.postUser.objects.filter(threads = channelName).exists():
                messages.error(request, 'this title already taken')
            else:
                 newChannel = models.postUser(creator = user, threads = channelName, descriptions = description,groupMembers = 1,timeCreated = now)
                 newChannel.save()
                 return redirect('home' , pk = channelName)
    return redirect('createNew')
@login_required(login_url='/login')
def profile(request, pk):
    user = request.user
    additional = models.UserLogin.objects.get(user = user)
    myThreads = models.postUser.objects.filter(creator = user)
    dic = {"pk":pk, "user":user, "info":additional, "myThreads": myThreads}
    return render(request, "profile/index.html",dic)
def create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password = request.POST.get('password')
        if (username and email and password1 and password ):
            if not(User.objects.filter(email = email).exists()):
                if not(User.objects.filter(username = username).exists()):
                    if (password == password1):
                        newUser = User(username = username, email = email, password = password, first_name = username)
                        newUser.set_password(password)
                        newUser.save()
                        newInfo = models.UserLogin(user = newUser, gender = "Ethiopia", profession = "Software Engineering")
                        newInfo.save()
                        return redirect('login')
                    else:
                        messages.error(request, "password is not similar")
                        return redirect("create")
                else:
                    messages.error(request, "username already taken")
                    return redirect("create")
            else:
                messages.error(request, "email already taken")
                return redirect("create")
                
    return render(request, "create/register.html")
def profileEdit(request,pk):
    user = request.user
    info = models.UserLogin.objects.get(user = user)
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        bio = request.POST.get('bio')
        profession = request.POST.get('profession')
        if (username and email):
            if not User.objects.filter(username=username).exclude(username=user.username).exists():
                 if not User.objects.filter(email=email).exclude(email=user.email).exists():
                     user.username = username
                     user.email = email                    
                     if fname:
                             user.first_name = fname
                     if lname:
                              user.last_name = fname
                     if bio:
                              user.bio = fname
                     if profession:
                              user.profession = fname
                     user.save()
                     return redirect('profile', pk = pk)
                 else:
                    messages.error(request, "email already exists")
            else:
                  messages.error(request, "username already exists")
       
        
    dic = {'user':user, "info" : info,"pk":pk}
    return render(request, "editProfile/edit_profile_form.html", dic)

def search_threads(request):
    query = request.GET.get('q', '')
    results = models.postUser.objects.filter(threads__icontains=query)[:5]
    data = {'results': [{'threads': result.threads} for result in results]}
    return JsonResponse(data)