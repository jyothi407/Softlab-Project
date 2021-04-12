from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart
from .models import History
from django.contrib.auth.models import User
from django.contrib import auth
#Shows details about statistics of orders made by user in the canteen so far.
def hist(request):
    his = History.objects.filter(customer=request.user).reverse()
    return render(request, 'history/history.html', {'his':his})
