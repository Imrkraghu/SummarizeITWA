# showcase/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.SummarizeIT, name="SummarizeIT"),
    path("rohit", views.rohit, name="rohit"),
    # path("<str:name>", views.greet, name="greet"),
    path("projects/", views.projects, name="projects"),
    path("team/", views.team, name="team"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact")
]