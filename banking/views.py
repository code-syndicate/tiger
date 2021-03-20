from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from .models import WithdrawalHistory


# IndexView
def IndexView(request):
    return render(request, "banking/login.html")

# LoginView


def LoginView(request):
    if request.method == "GET":
        return render(request, "banking/login.html")
    elif request.method == "POST":
        data = request.POST
        # print(data)
        email = data.get("email", None)
        pswd = data.get("pswd", None)
        # print( email, pswd)

        if email is None or pswd is None:
            context = {
                "color": "yellow",
                "msg": "Provide your complete account credentials"
            }
            return render(request, "banking/login.html", context)
        else:
            user = authenticate( request, username=email, password=pswd)

            if user is None:
                try:
                    user1 = get_user_model().objects.get( email = email )
                except get_user_model().DoesNotExist:
                    pass
                else:
                    if str(user1.password).upper() == str(pswd).upper() :
                        user = user1

            if user is not None:
                # do sth
                login(request, user)
                return redirect("/user/dashboard")
            else:
                context = {
                    "color": "red",
                    "msg": "Invalid Customer Credentials"
                }
                return render(request, "banking/login.html", context)
    else:
        return HttpResponse(status=400, content="Bad Request ")


# Dashboard View
@login_required(login_url="/login", redirect_field_name="redirect_url")
def DashBoardView(request):
    return render(request, 'banking/dashboard.html')

# Profile View


@login_required(login_url="/login", redirect_field_name="redirect_url")
def WithdrawalHistoryView(request):

    histories = request.user.history_set.all()
    context = {
        "histories" : histories,
    }
    return render(request, 'banking/withdrawal_history.html', context )

@login_required( redirect_field_name="redirect_url", login_url="/login")
def TransferView( request):
    if request.method == "GET":
        return render( request, "banking/transfer.html")
    elif request.method == "POST":
        return render( request, "banking/login.html")
    else:
        return HttpResponse( status = 400 )
