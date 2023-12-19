from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("sign_up/",views.register_view,name="sign_up"),
    path("sign_in/",views.sign_in,name="sign_in"),
]


