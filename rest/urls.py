from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = "rest"

urlpatterns = [
    path('home/',views.home,name="home"),
    path('book/',views.book,name="book"),
    path('about/',views.about,name="about"),
    path('menu/',views.menu,name="menu"),
]
