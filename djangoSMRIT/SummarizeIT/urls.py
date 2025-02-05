# showcase/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.SummarizeIT, name="SummarizeIT"),
]