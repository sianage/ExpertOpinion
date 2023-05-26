from django.urls import path, include

from . import views
from .views import UserRegisterView
#app_name = 'Members'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
]