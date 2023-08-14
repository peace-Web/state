from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Appartement
from .forms import AptForm, EditPost, EditProfile
from .filters import *
# Create your views here.

def logoutView(request):
    auth.logout(request) 
    return redirect("market")

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        username = request.POST["username"]
        phone = request.POST["phone"]

        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.warning(request, "email is already exists!")
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.warning(request, "username is already exists!")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username= username, email=email, password=password1)
                renter = Renter.objects.create(user = user, phone = phone)
                user.save()
                renter.save()
                messages.info(request, 'profile created successfully')
                auth.login(request, user)
                return redirect("market")
        else:
            messages.warning(request, 'passwords are not identical!')
            return redirect('register')
    return render(request, 'app/accounts/register.html')


def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("market")
        else:
            messages.warning(request, "username or password is incorrect!")
            return redirect("loginView")
    return render(request, "app/accounts/login.html")

def profile(request):
    user = request.user
    renter = Renter.objects.filter(user = user).first
    user_posts = Appartement.objects.filter(user = user)
    context = {"user_posts": user_posts, 'renter': renter}
    return render(request, 'app/accounts/profile.html', context)

def update_profile(request):
    renter = Renter.objects.get(user = request.user)
    form = EditProfile(instance = renter)
    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES , instance = renter)
        # form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect("update_profile")
        else:
            print(form.errors.as_data())
    context = {"renter": renter, 'form': form}
    return render(request, 'app/accounts/update_profile.html', context)

def index(request):
    return render(request, 'app/index.html')

def market(request):
    apts = Appartement.objects.filter(occupied = False, status = "Show").order_by("city")
    filter = OrderFilter(request.GET, queryset = apts)
    apts = filter.qs
    context = {"apts": apts, "filter":filter}
    
    return render(request, 'app/market/main.html', context)


def publish(request):
    if request.user.is_authenticated: 
        renter = Renter.objects.get(user = request.user)
        form = AptForm()
        if request.method == "POST":
            form = AptForm(request.POST, request.FILES)
            form.instance.user = request.user
            form.instance.renter = renter
            if form.is_valid():
                form.save()
                return redirect("market")
            else:
                print(form.errors.as_data())
        context = {"form": form}
        return render(request, 'app/publish.html', context)
    else:
        messages.info(request, "Cant publish without login!, sign in please")
        return redirect("loginView")
    
def editpost(request, pk):
    post = Appartement.objects.get(id = pk)
    form = EditPost(instance=post)
    if request.method == "POST":
        form = EditPost(request.POST,  request.FILES, instance=post)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors.as_data())

    context = {"form": form}
    return render(request, 'app/accounts/edit.html', context)

def delete(request, pk):
    post = Appartement.objects.get(id = pk)
    if request.method =="POST":
        post.delete()
        return redirect("profile")
    context = {"post": post}
    return render(request, "app/accounts/deletepost.html", context)

def view_post(request, pk):
    post = Appartement.objects.get(id = pk)
    context = {"post": post}
    return render(request, 'app/market/view_post.html', context)

def contactowner(request, pk):
    post = Appartement.objects.get(id = pk)
    context = {"post": post}
    return render(request, 'app/contact_owner/contact_owner.html', context)