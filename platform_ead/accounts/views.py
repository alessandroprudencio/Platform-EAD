from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)

from django.contrib.auth import authenticate ,login, logout, get_user_model

from django.conf import  settings

from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegisterForm,EditAccountForm, PasswordResetForm

from django.contrib.auth.decorators import login_required

from .models import PasswordReset

from platform_ead.courses.models import Enrollment

from django.contrib import messages


from platform_ead.core.utils  import generate_hash_key

User = get_user_model()

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

def password_reset(request):
    template_name = 'reset/reset_password.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] =True

    context['form'] = form

    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'reset/confirm_new_password.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST  or None)
    print(form)

    if form.is_valid():
        print('entru')
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

@login_required
def dashboard(request):
    template_name = 'dashboard/dashboard.html'
    context = {}
    return render (request, template_name, context)

@login_required
def edit(request):
    template_name = 'dashboard/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados foram alterados com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error ao atualizar dados!')
        context['form'] = form

    return render(request, template_name,context)
