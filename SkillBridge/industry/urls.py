from django.urls import path
from . import views

urlpatterns = [
    path("", views.industry_dashboard, name="industry_dashboard"),
]
