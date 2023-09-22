from django.shortcuts import render, redirect
from django.http import HttpResponse, request, HttpResponseRedirect
from . models import Gallery, UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator  # for pages eg next, previous pages
import json

# Create your views here.
def home_page(request, *args, **kwargs):
    if request.method == "POST":
        uname = request.POST['uname']
        fname = request.POST['fname']
        sname = request.POST['sname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        try:
            if password == password2: 
                current_user = User.objects.create(
                    username = uname,
                    first_name = fname,
                    last_name = sname,
                    email = email,
                    password = password
                )
                print(current_user.id)
                if request.FILES:
                    pp = request.FILES['pp']
                    UserProfile.objects.create(
                        pp = pp,
                        owner = User.objects.get(id = current_user.id)
                    )
                messages.info(request, "Account creation successful")
            else:
                print("Passwords do not match!")
                messages.info(request, "Passwords do not match!!")
        except:
            print("User already exists!")
            messages.info(request, "User already exists!")
        print(request.POST)
    context = {
    }
    response = render(request, "index.html", context)
    response.set_cookie("name","EngLovis")
    return response

@login_required(login_url="/login/")
def about_page(request, *args, **kwargs):
    context = {
    }
    response = render(request, "about.html", context)
    response.set_cookie("name","EngDave")
    return response

def login_page(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return redirect("/about/")
        else:
            messages.info(request,"Invalid Credentials")

    context = {
    }
    response = render(request, "login.html", context)
    response.set_cookie("name","EngDave")
    return response

# @login_required(login_url= "/login/")      dont require login first
def gallery_page(request, *args, **kwargs):
    if request.method =="POST":
        id = request.POST['id']
        caption = request.POST['caption']
        gallery_item_to_update = Gallery.objects.get(id=id)
        gallery_item_to_update.caption = caption
        if request.FILES:
            if gallery_item_to_update.pic != "gallery/default.jpg":
                gallery_item_to_update.pic.delete()
            pic = request.FILES['pic']
            gallery_item_to_update.pic =pic
        gallery_item_to_update.save()
        return HttpResponse(json.dumps({"message":"update successfull"}))


    next = request.GET.get("page")
    delete = request.GET.get("delete")
    update = request.GET.get("update")
    # update image
    if update:
        item_to_update = Gallery.objects.get(id=update)
        context = {
            "gallery":item_to_update
        }
        return render(request, "update.html", context)
    if delete:
        item_to_delete = Gallery.objects.get(id=delete)

        if item_to_delete.pic != "gallery/default.jpg":
            item_to_delete.pic.delete()
        item_to_delete.delete()
        return redirect("/gallery/")

    gallery_items = Gallery.objects.all().order_by("-id")
    paginated = Paginator(gallery_items, 6)
    if next:
        paged = paginated.get_page(next)
    else:
        paged = paginated.get_page(1)
    context = {
        "gallery_items":paged
    }
    response = render(request, "gallery.html", context)
    response.set_cookie("name","EngDave")
    return response
#require user to login to access aboutUs and gallery pages
@login_required(login_url="/login/")
def about_page(request, *args, **kwargs):
    context = {
    }
    response = render(request, "about.html", context)
    return response
# Home page view
def home(request, *args, **kwargs):
    context = {
    }
    response = render(request, "home.html", context)
    return response
# address view
def address_page(request, *args, **kwargs):
    context = {
    }
    response = render(request, "address.html", context)
    return response
# contact us view
def contact_page(request, *args, **kwargs):
    context = {
    }
    response = render(request, "contact.html", context)
    return response
# book view
def book_page(request, *args, **kwargs):
    context = {
    }
    response = render(request, "book.html", context)
    return response
def start_page(request, *args, **kwargs):
    context = {
    }
    response = render(request, "index.html", context)
    return response

