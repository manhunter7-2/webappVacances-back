from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("test", views.create, name="create"),
    path("create", views.createAccount, name="createAccount")
]