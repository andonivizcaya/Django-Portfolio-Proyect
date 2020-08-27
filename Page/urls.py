from django.urls import path
from Page import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('project01', views.project01, name="Project01"),  
    path('project02', views.project02, name="Project02"),
    path('external', views.external),
]