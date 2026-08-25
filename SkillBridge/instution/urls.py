from django.urls import path
from . import views

urlpatterns = [
    path("", views.instution_dashboard, name="instution_dashboard"),
]