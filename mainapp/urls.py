from django.urls import path
from . import views

urlpatterns = [
    path('count/<int:angka>/', views.count),
    path('sapa/<str:nama>/', views.sapa),
    path('example/', views.example),
    path('profile/', views.profile),
    path('second/', views.second_page),
    path('', views.landing_page),
    path('resume-nova/', views.resume_nova),
    path('toko-nova/', views.toko_nova),

]
