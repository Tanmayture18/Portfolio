from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("education",views.education,name='education'),
    path("experience",views.experience,name='experience'),
    path("projects",views.projects,name='projects'),
    path("certifications",views.certifications,name='certifications')
]
