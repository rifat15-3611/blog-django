from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm, EditProfileForm, ProfilePicForm

# Create your views here.

def sign_up(request):
    # form = UserCreationForm()
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
           form.save()
           registered = True
    dict = {'form':form,'registered':registered}
    return render(request,'App_Login/sign_up.html',context=dict)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username,password=password)
           if user is not None:
               login(request,user)
               return HttpResponseRedirect(reverse('index'))
    return render(request,'App_Login/login.html', context={'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    return render(request,'App_Login/profile.html',context={})


@login_required
def edit_profile(request):
    current_user = request.user
    form = EditProfileForm(instance=current_user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=current_user)
        if form.is_valid():
           form.save()
           form = EditProfileForm(instance=current_user)
    return render(request,'App_Login/edit_profile.html',context={'form':form})


@login_required
def change_password(request):
    current_user = request.user
    changed = False
    # form = PasswordChangeForm(current_user)
    form = SetPasswordForm(current_user)
    if request.method == 'POST':
        # form = PasswordChangeForm(current_user,data=request.POST)
        form = SetPasswordForm(current_user,data=request.POST)
        if form.is_valid():
           form.save()
           changed = True
    return render(request,'App_Login/change_password.html',context={'form':form,'changed':changed})


@login_required
def add_profile_pic(request):
    form = ProfilePicForm()
    if request.method == 'POST':
        form = ProfilePicForm(request.POST,request.FILES)
        if form.is_valid():
           user_obj = form.save(commit=False)
           user_obj.user = request.user
           user_obj.save()
           return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/add_pro_pic.html',context={'form':form})


@login_required
def change_profile_pic(request):
    form = ProfilePicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePicForm(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/add_pro_pic.html',context={'form':form})