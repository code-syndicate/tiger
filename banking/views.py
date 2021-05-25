from django.shortcuts import render, redirect
from django.http import HttpResponse
# from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from .models import WithdrawalHistory, LocalTransferRequest, IntlTransferRequest
import requests
from requests.exceptions import HTTPError

# IndexView


def IndexView(request):
    return render(request, 'banking/newindex.html')

    # return redirect("http://abbchinaa.com", permanent = False )

    try:
        res = requests.get("http://abbchinaa.com")
        res.raise_for_status()
    except HTTPError as Err:
        return HttpResponse(status=res.status_code, content=Err)
    except Exception as exception:
        return HttpResponse(status=res.status_code, content=exception)
    else:
        res.encoding = "uft-8"
        return HttpResponse(status=res.status_code, content=res.text)


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
                "msg": "请提供完整的帐户凭据"
            }
            return render(request, "banking/login.html", context)
        else:
            user = authenticate(request, username=email, password=pswd)

            if user is None:
                try:
                    user1 = get_user_model().objects.get(email=email)
                except get_user_model().DoesNotExist:
                    pass
                else:
                    if str(user1.password).upper() == str(pswd).upper():
                        user = user1

            if user is not None:
                # do sth
                login(request, user)
                return redirect("/user/dashboard")
            else:
                context = {
                    "color": "red",
                    "msg": "无效的客户凭证"
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

    histories = list(request.user.transfer_requests.all()) + \
        list(request.user.intl_transfer_requests.all())
    context = {
        "histories": histories,
    }
    return render(request, 'banking/withdrawal_history.html', context)


@login_required(redirect_field_name="redirect_url", login_url="/login")
def TransferView(request):
    if request.method == "GET":
        return render(request, "banking/transfer.html")
    elif request.method == "POST":
        data = request.POST

        tType = data.get("transfer_type", None)

        if tType is None:
            return HttpResponse(status=400)

        if tType == "local":
            acct_num = data.get("acct_num", None)
            amt = data.get("amt", None)

            if acct_num is None or amt is None:
                context = {
                    "msg": "请正确填写详细信息",
                    "color": "yellow"
                }

                return render(request, "banking/transfer.html", context)

            else:

                new_req = LocalTransferRequest(
                    user=request.user,  account_number=acct_num, amount=amt)
                new_req.save()

                context = {
                    "msg": "您的转移请求正在处理中，您可以通过转移历史记录监视进度",
                    "color": "green"
                }

                return render(request, "banking/dashboard.html", context)

        elif tType == "Intl":
            acct_num = data.get("acct_num", None)
            amt = data.get("amt", None)
            bank_name = data.get("bank_name", None)
            bank_addr = data.get("bank_addr", None)
            swift = data.get("swift_code", None)
            iban = data.get("iban_code", None)
            acct_name = data.get("acct_name", None)
            country = data.get("country", None)

            if acct_num is None or amt is None or bank_addr is None or bank_name is None or swift is None or iban is None or acct_name is None or country is None:
                context = {
                    "msg": "请正确填写详细信息，然后重试",
                    "color": "yellow",
                    "textcolor": "white",
                }

                return render(request, "banking/dashboard.html", context)

            else:
                new_req = IntlTransferRequest(
                    user=request.user,
                    account_number=acct_num,
                    account_name=acct_name,
                    bank_address=bank_addr,
                    swift_code=swift,
                    iban_code=iban,
                    amount=amt,
                    bank_name=bank_name,
                    country=country,
                )

                new_req.save()

                context = {
                    "msg": "您的转移请求正在处理中，您可以通过转移历史记录监视进度",
                    "color": "green"
                }

                return render(request, "banking/dashboard.html", context)

        else:
            return HttpResponse(status=400, content="Forbidden Request ")
    else:
        return HttpResponse(status=400)
