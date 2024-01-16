from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Borrowbook.models import Borrowedbook
from django.views import View
from .forms import ChangeUserForm

# Create your views here.
def sing_up(request):
    if request.method == 'POST':
        sing_up_form = forms.SingForm(request.POST)
        if sing_up_form.is_valid():
            sing_up_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('user_login')
    
    else:
        sing_up_form = forms.SingForm()
    return render(request, 'authentication/register.html', {'form' : sing_up_form, 'type' : 'sing_up'})

class Loginview(LoginView):
    template_name = 'authentication/register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('user_login')

class UpdateView(View):
    template_name = 'authentication/update_profile.html'

    def get(self, request):
        form = ChangeUserForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})

@login_required
def profile(request):
    data = Borrowedbook.objects.filter(user=request.user)
    return render(request,'authentication/profile.html',{'dataa':data})


