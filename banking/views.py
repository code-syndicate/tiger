from django.shortcuts import render
from django.http import HttpResponse


# IndexView 
def IndexView( request):
    return render( request, "banking/login.html")


#Dashboard View
def DashBoardView(request):
    return render( request, 'banking/dashboard.html')