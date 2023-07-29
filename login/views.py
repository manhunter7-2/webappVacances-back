from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
import environ
import hashlib
from login.models import User
from django.core.mail import send_mail, EmailMessage, get_connection
from django.conf import settings

env = environ.Env()
environ.Env.read_env()
salt = env("SALT")

def index(request):
    return HttpResponse("Hello World !")

@csrf_exempt
def login(request):
    if request.method == "POST":
        # sendMail()
        try:
            pwd = request.POST.get("password")
            pwd = pwd+salt
            pwd=hashlib.md5(pwd.encode()).hexdigest()
            user = User.objects.get(name=request.POST.get("name"), password=pwd)
        except User.DoesNotExist:
            return HttpResponse("No account found")
    return HttpResponse("SUCCESS !")

@csrf_exempt
def createAccount(request):
    if request.method == "POST":
        name = request.POST.get("name")
        pwd = request.POST.get("password")
        pwd = pwd+salt
        pwd = hashlib.md5(pwd.encode())
        try:
            user=User.objects.get(name=name)
        except User.DoesNotExist:
            print("HASHED : ", pwd.hexdigest()) #WORKING
            login = User(name=name, password=pwd.hexdigest())
            login.save()
            return HttpResponse(pwd.hexdigest())
    return HttpResponse("Account already exists")


@csrf_exempt
def testMail(request):
    if request.method == "POST":
        with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password = settings.EMAIL_HOST_PASSWORD,
            use_tls = settings.EMAIL_USE_TLS
        ) as connection:
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email"), ]
            message = request.POST.get("message")
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
    return render(request, 'test.html')