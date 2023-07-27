from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
import environ
import hashlib
from login.models import Login

env = environ.Env()
environ.Env.read_env()
salt = env("SALT")

def index(request):
    return HttpResponse("Hello World !")

# @ensure_csrf_cookie
@csrf_exempt
def create(request):
    if request.method == "POST":
        print(request.POST.get("test"))
    return 0

@csrf_exempt
def createAccount(request):
    # if request.method == "POST":
    name = request.POST.get("name")
    pwd = request.POST.get("password")
    pwd = pwd+salt
    pwd = hashlib.md5(pwd.encode())
    print("HASHED : ", pwd.hexdigest()) #WORKING
    login = Login(name=name, password=pwd)
    login.save()
    return 1
        
        

# Create your views here.
