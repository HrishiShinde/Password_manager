from django.shortcuts import render
from django.http import JsonResponse
from PMapp.models import User
from django.db import connection,transaction

# Create your views here.
def logshow(request):
    return render(request, "login.html")

def dologin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        upass = request.POST.get("password")

        for u in User.objects.raw('select * from User where userName="%s" and userPass="%s"' % (uname, upass)):
            if u.userName == uname:
                request.session['user'] = uname
                return render(request, "home.html", {"success":"Welcome " + u.userName+ ", Your safe is ready!"})
        else:
            return render(request, "login.html", {"fail":"Login failed, Please enter your Username and password correctly!"})

def regshow(request):
    return render(request, "register.html")

def doregister(request):
    if request.method == "POST":
        uname = request.POST.get('name')
        umail = request.POST.get('email')
        upass = request.POST.get('pass')

        cursor = connection.cursor()
        query = "insert into User(userName, userEmail, userPass) values('%s', '%s', '%s')" % (uname, umail, upass)
        cursor.execute(query)
        transaction.commit()

        request.session['user'] = uname
        #return render_template('simple.html',data=json.dumps(name))
        return render(request, "home.html", {"success":"Welcome " + uname + ", Your safe is created!"})

def showap(request):
    return render(request, "addpass.html", {"username" : request.session['user']})

def storepass(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        sname = request.POST.get('sname')
        upass = request.POST.get('pass')

        cursor = connection.cursor()
        query = "insert into Password(userName, siteName, sitePass) values('%s', '%s', '%s')" % (uname, sname, upass)
        cursor.execute(query)
        transaction.commit()

        return render(request, "home.html", {"success":"Your password was stored safe in your Safe!"})
