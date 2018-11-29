from django.shortcuts import render, redirect

# Create your views here.

def change_currency(request):
    request.session["currency"]=request.POST.get("currency", "EUR")
    print(request.POST)
    return redirect(request.POST["redirect_to"])
