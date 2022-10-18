from django.urls import path
from .views import UserCreateView, UserEditView
urlpatterns = [

    path('register/', UserCreateView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),


]  