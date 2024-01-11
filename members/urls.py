from django.urls import path, include
from .views import UserRegistationView

urlpatterns = [
    path("registation/", UserRegistationView.as_view(), name="registation")
]
