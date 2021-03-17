from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# IndexView 
def IndexView( request):
    return render( request, "banking/login.html")


#Dashboard View
@login_required
def DashBoardView(request):
    return render( request, 'banking/dashboard.html')
    
#Profile View
@login_required
def ProfileView(request):
    return render( request, 'banking/profile.html')