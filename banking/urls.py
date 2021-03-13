from django.urls import path
from .import views

urlpatterns = [
    path( '', views.IndexView, name = "indexview "),
    path('dashboard/', views.DashBoardView, name = "dashboardview"),

]