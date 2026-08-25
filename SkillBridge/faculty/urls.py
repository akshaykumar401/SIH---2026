from django.urls import path
from . import views

urlpatterns = [
    path("", views.faculty_dashboard, name="faculty_dashboard"),
]