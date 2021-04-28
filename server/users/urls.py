from django.urls import path, include
from .views import *

urlpatterns = [
    path('register-user', include('users.urls')),
    path('login-user', include('quizes.urls')),
]
