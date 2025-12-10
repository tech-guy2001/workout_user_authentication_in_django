from django.contrib import admin
from django.urls import path,include

from userapp.views import home,aboutpage

# urlpatterns = [
#     path('home',home),
#     path('about',aboutpage),
# ]


from .views import register_view, login_view, logout_view,home

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('home',home),
    # ...
]