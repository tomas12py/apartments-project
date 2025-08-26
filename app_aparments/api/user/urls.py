from app_aparments.api.user.views import UserRegister
from django.urls import path

urlpatterns = [
    path("user/", UserRegister.as_view()),  
    path("user/<id>/", UserRegister.as_view()),
]
