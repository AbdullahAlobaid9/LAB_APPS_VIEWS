from django.urls import path

from . import views

app_name = "HelloPage"

urlpatterns = [
    path("home/", views.home, name="home")
]