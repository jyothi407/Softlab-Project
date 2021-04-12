from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart
from .models import History
from django.contrib.auth.models import User
from django.contrib import auth#necessary librarys imported
def hist(request):#hist function
    his = History.objects.filter(customer=request.user).reverse()#data retrival from postgresql
    return render(request, 'history/history.html', {'his':his})# returns render
