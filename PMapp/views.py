from django.shortcuts import render
from django.http import JsonResponse
from PMapp.models import User,Password
from django.db import connection,transaction
from cryptography.fernet import Fernet
from secret_file import enc_pass, dec_pass, pass_hash
import random, pyperclip

# Create your views here.
def logshow(request):
    return render(request, "login.html")

def dologin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        upass = request.POST.get("password")

        upass = pass_hash(upass)

        for u in User.objects.raw('select * from User where userName="%s"' % (uname)):
            if u.userPass == upass:
                print(upass,"<----Entered pass||DB pass---->",u.userPass,type(u.userPass))
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
 
        #upass = str(pass_hash(upass))[2:-1]
        upass = pass_hash(upass)

        cursor = connection.cursor()
        query_obj = User.objects.create(userName = uname, userEmail = umail, userPass = upass)
        query_obj.save()

        request.session['user'] = uname
        #return render_template('simple.html',data=json.dumps(name))
        return render(request, "home.html", {"success":"Welcome " + uname + ", Your safe is created!"})

def showap(request):
    return render(request, "addpass.html", {"username" : request.session['user']})

def storepass(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        sname = request.POST.get('sname')
        spass = request.POST.get('pass')

        for u in User.objects.raw('select * from User where userName="%s"' % (uname)):
            upass = u.userPass
        
        
        renc_pass = enc_pass(spass,uname)

        cursor = connection.cursor()
        query_obj = Password.objects.create(userName = uname, siteName = sname, sitePass = renc_pass)
        query_obj.save()

        return render(request, "home.html", {"success":"Your password was stored safe in your Safe!"})

def genpass(request):
    chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*?"
    password=""
    for i in range(8):
        pass_char = random.choice(chars)
        password = password + pass_char

    pyperclip.copy(password)
    #spam = pyperclip.paste()

    data = {"pass" : password, "ctcb" : "copied"}
    return JsonResponse(data)

def showpass(request):
    uname = request.session['user']
    sitename = []
    sitepass = []
    data = {}
    for s in Password.objects.raw('select * from Password where userName="%s"' % (uname)):
        sin = s.siteName
        sip = s.sitePass

        sitename.append(sin)
        sitepass.append(str(dec_pass(uname, sip))[2:-1])
        data[sin] = str(dec_pass(uname, sip))[2:-1]
        break
    else:
        return render(request, "home.html", {"no_pass": "You haven't stored any passwords yet!"})
    
    #data = Password.objects.raw('select * from Password where userName="%s"' % (uname))

    print(sitename)
    print(sitepass)
    print(data)
    #rdec_pass = str(dec_pass(uname, sitepass))[2:-1]
    #data = {"pass": sitepass, "sitename" : sitename}

    return render(request, "home.html", data)

