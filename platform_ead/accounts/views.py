from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.contrib.auth import authenticate ,login, logout

from django.conf import  settings

from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegisterForm,EditAccountForm

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

@login_required
def edit(request):
    template_name = 'dashboard/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form = EditAccountForm(instance=request.user)
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.errors:
                 context['success'] = False
            else:
                form.save()
                context['success'] = True
                return redirect(settings.DASHBOARD_URL)
        else:
            print('não passo valid')
            form = EditAccountForm(instance=request.user)
        context['form'] = form

    return render(request, template_name,context)