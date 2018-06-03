from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.models import UserProfile
from links.models import Link
from users.validate import validate_account


# === Funkcje reprezentujące widoki aplikacji users:  ===

"""
Funkcja odpowiedzialna za generowanie strony logowania/rejestracji.
"""
def login_site(request):
    return render(request, 'users/login.html', {})


"""
Funkcja wywoływana w momencie próby zalogowania. Sprawdza poprawność 
wprowadzonych danych.
"""
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main_page')
    else:
        messages.add_message(request, messages.ERROR,
                             'Username or password not correct')
        return redirect('login_site')


@login_required
def log_out(request):
    logout(request)
    return redirect('main_page')


"""
Funkcja służąca do tworzenia konta uzytkownika. Przy pomocy funkcji 
validate_accountsprawdzane są dane pobrane z formularza w szablonie - jeśli 
są poprawne, tworzone jest konto, w przeciwnym przypadku wyświetlany 
jest komunikat z błędem.

"""
def create_account(request):
    if request.method == 'POST':
        form_data = request.POST
        username = form_data['username']
        email = form_data['email']
        password = form_data['password']
        conf_password = form_data['confirm_password']
        if validate_account(username, email, password, conf_password):
            message = validate_account(username, email, password, conf_password)
            messages.add_message(request, messages.ERROR, message)
            return redirect('login_site')
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        UserProfile.objects.create(user=user)
        login(request, user)
        return redirect('main_page')


"""
Funkcja służąca do generowania profilu użytkownika.
"""
@login_required
def user_profile(request):
    user = request.user
    author = UserProfile.objects.get(user=user)
    links = Link.objects.filter(author=author)
    context = {
        'links': links,
    }
    return render(request, 'users/user_profile.html', context)


@login_required
def post_link(request):
    return render(request, 'users/post_link.html', {})

