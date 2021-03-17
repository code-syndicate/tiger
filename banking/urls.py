from django.urls import path
from .import views

urlpatterns = [
    path( '', views.IndexView, name = "indexview "),
    
    path( 'login', views.LoginView, name = "Loginview "),
    path('user/dashboard/', views.DashBoardView, name = "dashboardview"),
    
    path('user/profile/', views.ProfileView, name = "profileview"),

]