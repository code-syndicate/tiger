from django.urls import path
from .import views


app_name = "banking"

urlpatterns = [
    
    path( 'login/', views.LoginView, name = "Loginview "),
    path( '', views.IndexView, name = "indexview "),
    
    path('user/dashboard/', views.DashBoardView, name = "dashboardview"),
    
    path('user/transfer-history/', views.WithdrawalHistoryView, name = "historyview"),
    
    path('user/transfer/', views.TransferView, name = "transferview"),
]