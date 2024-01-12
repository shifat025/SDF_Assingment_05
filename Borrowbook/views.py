from django.shortcuts import render,redirect
from Book.models import Books
from .models import Borrowedbook
from transaction.models import account
from transaction.views import send_transaction_email
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def borrow(request, id):
    data = Books.objects.get(pk=id)
    useraccount = request.user.account
    quntity = data.quantity
    price = data.borrowing_price
    balance = useraccount.account_balance

    if balance > price and quntity > 1:
        quntity -=1
        balance -= price
        useraccount.account_balance = balance
        useraccount.save()
        data.quantity = quntity
        data.save()
        borrow=Borrowedbook.objects.create(user=request.user, books=data)
        send_transaction_email(request.user,price, "BookBorrow Message", "borrow.html")  
        return redirect('profile')
    return render(request,'authentication/profile.html',{'book':data})
@login_required
def bookreturn(request, id, historyid):
    data = Books.objects.get(pk=id)
    useraccount = request.user.account
    quntity = data.quantity
    price = data.borrowing_price
    balance = useraccount.account_balance

    if  price:
        quntity +=1
        balance += price
        useraccount.account_balance = balance
        useraccount.save()
        data.quantity = quntity
        data.save()
        pharses=Borrowedbook.objects.get(id=historyid)
        pharses.delete()
        return redirect('profile')
    return render(request,'authentication/profile.html',{'book':data})