from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from educationsite.forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/reminder/')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/reminder/')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/account/login/')
