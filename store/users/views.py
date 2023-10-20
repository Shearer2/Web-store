from django.shortcuts import render, HttpResponseRedirect
# Импортируем приложение auth, чтобы узнать существует ли пользователь.
from django.contrib import auth, messages
from django.urls import reverse

from users.models import User
# Импортируем класс, чтобы присоединить форму к приложению.
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


# Create your views here.
# Контроллер для авторизации.
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


# Контроллер для регистрации.
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # Если форма валидна, то необходимо сохранить объект в базе данных.
            form.save()
            # Выводим сообщение пользователю об успешной регистрации.
            messages.success(request, 'Поздравляем! Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


# Контроллер для профиля.
def profile(request):
    if request.method == 'POST':
        # Чтобы можно было изменять данные и сохранять их, необходимо указать не просто data, но и instance.
        # При помощи переменной files передаётся изменённое изображение.
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        # Данные должны быть как при GET запросе, так и при POST запросе.
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Store - Профиль', 'form': form}
    return render(request, 'users/profile.html', context)


# Контроллер для выхода из системы.
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
