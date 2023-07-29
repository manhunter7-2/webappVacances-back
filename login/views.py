from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
import environ
import hashlib
from login.models import User
from django.core.mail import send_mail

env = environ.Env()
environ.Env.read_env()
salt = env("SALT")

def index(request):
    return HttpResponse("Hello World !")

@csrf_exempt
def login(request):
    if request.method == "POST":
        sendMail()
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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = False
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'your@djangoapp.com'
EMAIL_HOST_PASSWORD = 'your password'
        