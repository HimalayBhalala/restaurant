from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.conf import settings
from .models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

User = settings.AUTH_USER_MODEL

@login_required
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Hey {username},Your account was created successfully...")
            new_user = authenticate(username=form.cleaned_data['email'],password=form.cleaned_data["password1"])
            login(request,new_user) 
            return redirect("rest:home")        
    else:
        form = UserRegisterForm()
    context = {
        'form':form,
        'messages':messages,
    }
    return render(request,'userauths/sign_up.html',context)

def sign_in(request):
    # if request.user.is_authenticated:
    #     return redirect("home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request,f"User with {{email}} does not exits")

        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"you are Logged Successfully.....")
            return redirect("rest:home")
        else:
            messages.warning(request,"User Does not exits,create an account")

    context = {
        'messages' : messages
    }
    return render(request,'userauths/sign_in.html',context)