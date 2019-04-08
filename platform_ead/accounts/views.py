from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate ,login, logout

from django.conf import  settings

from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegisterForm

from django.contrib.auth.decorators import login_required

def register(request):
    template_name = 'registration/register.html'

    if request.method == "POST":
        form  = RegisterForm(request.POST)
        if form.is_valid():
           user = form.save()
           user = authenticate(username=user.username, password=form.cleaned_data['password1'])
           login(request, user)
           return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form =  RegisterForm()

    context= {
        'form':form
    }
    return render(request, template_name, context)

@login_required
def dashboard(request):
    template_name = 'dashboard/dashboard.html'
    return render (request, template_name)