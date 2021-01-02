from django.shortcuts import render
from django.http import JsonResponse
from PMapp.models import User

# Create your views here.
def logshow(request):
    return render(request, "login.html")

def dologin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        upass = request.POST.get("password")

        for u in User.objects.raw('select * from User where userName="%s" and userPass="%s"' % (uname, upass)):
            if u.userName == uname:
                request.session['user_entered'] = uname
                return render(request, "home.html", {"success":"Welcome " + u.userName})
        else:
            return render(request, "login.html", {"fail":"Login failed, Please enter your Username and password correctly!"})
