from django.shortcuts import render, redirect
from . import forms
from .models import account
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


# Create your views here.
def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

@login_required
def deposit(request):
    if request.method == 'POST':
        dep_form = forms.AccountForm(request.POST)
        if dep_form.is_valid():
            amount = dep_form.cleaned_data.get('diposit')
            user_account = request.user.account
            user_account.account_balance += amount
            user_account.save()
            send_transaction_email(request.user, amount, "Deposite Message", "deposit_mail.html")  
            return redirect('deposit')
           
    else:
        dep_form = forms.AccountForm()
    return render(request,'deposit.html',{'form':dep_form})

