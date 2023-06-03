from django.urls import path, include

from . import views
from .views import UserRegisterView, UserEditView, ProfileView

#app_name = 'Members'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('<int:pk>/profile/', ProfileView.as_view(), name="profile_page"),
]