from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(req):
    if req.method=='POST':
        form= UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(req, f'Your account has been created. You are able to Login!')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(req,'user/register.html',{'form':form})

@login_required
def profile(req):
    if req.method=='POST':
        u_form=UserUpdateForm(req.POST,instance=req.user)
        p_form=ProfileUpdateForm(req.POST,req.FILES,instance=req.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(req,f'Your account has been updtaed!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=req.user)
        p_form=ProfileUpdateForm(instance=req.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(req,'user/profile.html',context)