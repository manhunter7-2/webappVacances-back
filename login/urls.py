from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("create", views.createAccount, name="createAccount"),
    path("login", views.login, name="login")
]