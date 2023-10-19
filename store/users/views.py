from django.shortcuts import render, HttpResponseRedirect
# Импортируем приложение auth, чтобы узнать существует ли пользователь.
from django.contrib import auth
from django.urls import reverse

from users.models import User
# Импортируем класс, чтобы присоединить форму к приложению.
from users.forms import UserLoginForm, UserRegistrationForm


# Create your views here.
def login(request):
    # Чтобы проверить какой запрос пришёл необходимо сделать условие, так как данная страница будет работать на два
    # запроса, предоставление информации пользователю GET и получение информации о пользователе POST.
    if request.method == 'POST':
        # Если происходит POST запрос на получение информации о клиенте сервером, то необходимо передавать данные.
        form = UserLoginForm(data=request.POST)
        # Необходимо делать проверку на валидность.
        if form.is_valid():
            # Если данные проходят валидацию, то необходимо достать данные, которые пришли.
            username = request.POST['username']
            password = request.POST['password']
            # Необходимо достать данного пользователя из базы данных, чтобы понять существует ли он вообще.
            # Чтобы узнать есть ли данный пользователь передаём его имя и пароль.
            user = auth.authenticate(username=username, password=password)
            # Если пользователь есть, то мы его авторизуем, передавая запрос и пользователя.
            if user:
                auth.login(request, user)
                # Перенаправляем пользователя после авторизации на главную страницу.
                # Если в reverse передать название пути из файла urls.py, то он возвращает адрес.
                return HttpResponseRedirect(reverse('index'))
    else:
        # Если происходит GET запрос, то возвращаем нашу форму.
        form = UserLoginForm()
    # Обращаемся через ключ к нашей форме, чтобы она отображалась.
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # Если форма валидна, то необходимо сохранить объект в базе данных.
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)
