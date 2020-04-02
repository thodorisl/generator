from django.urls import path
from generator import views

app_name = 'generator'
urlpatterns = [
    path('', views.home,),
    path('password/', views.password),
    path('about/', views.about, ),
]
