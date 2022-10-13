from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .forms import NewUserForm
from django.contrib import messages

def user_login(request):
    if request.GET.get('action') == 'login':
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('main:home')
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if request.GET.get('action') == 'registration':
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                #messages.success(request, "Registration successful.")
                return redirect('main:home')
            #messages.error(request, "Unsuccessful registration. Invalid information.")
        else:
            form = NewUserForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('main:home')


def account_page(request):
    return render(request, 'account.html')



