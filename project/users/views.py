from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title':'Register'})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title':'Profile'})

@login_required
def update_profile(request):
    if request.method == 'POST':
        u_update_form = UserUpdateForm(request.POST, instance=request.user)
        p_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_update_form.is_valid() and p_update_form.is_valid():
            u_update_form.save()
            p_update_form.save()
            messages.success(request, f'Update successful')
            return redirect('profile')
    else:
        u_update_form = UserUpdateForm(instance=request.user)
        p_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_update_form': u_update_form,
        'p_update_form': p_update_form,
        'title': 'Profile'
    }

    return render(request, 'users/update_prof.html', context)