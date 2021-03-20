from django.urls import path
from .import views


app_name = "banking"

urlpatterns = [
    path( '', views.IndexView, name = "indexview "),
    
    path( 'login', views.LoginView, name = "Loginview "),
    path('user/dashboard/', views.DashBoardView, name = "dashboardview"),
    
    path('user/transfer-history/', views.WithdrawalHistoryView, name = "historyview"),
    
    path('user/transfer/', views.TransferView, name = "transferview"),
]