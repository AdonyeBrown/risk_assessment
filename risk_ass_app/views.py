from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request,  "risk_ass_app/index.html")


def signup(request):
    if request.method == "POST":
        # username = request.POST.get("username")
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect("signin")

    return render(request, "risk_ass_app/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "risk_ass_app/index.html", {"fname": fname})
        else:
            messages.error(request, "Wrong Credentials!")
            return redirect("home")

    return render(request, "risk_ass_app/signin.html")


def signout(request):
    pass
