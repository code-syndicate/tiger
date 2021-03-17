from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# IndexView 
def IndexView( request):
    return render( request, "banking/login.html")

# LoginView 
def LoginView( request):
    return render( request, "banking/login.html")


#Dashboard View
@login_required( login_url="/login")
def DashBoardView(request):
    return render( request, 'banking/dashboard.html')
    
#Profile View
@login_required(login_url="/login")
def ProfileView(request):
    return render( request, 'banking/profile.html')