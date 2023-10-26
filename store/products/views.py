from django.shortcuts import render, HttpResponseRedirect
# Подключаем модуль, который не будет обрабатывать контроллер, пока не будет произведена авторизация.
from django.contrib.auth.decorators import login_required

from products.models import ProductCategory, Product, Basket
# Импортируем пагинатор для пагинации страниц.
from django.core.paginator import Paginator


# Create your views here.
# Функции = контроллеры = вьюхи.
# Функция для отображения файла index.html.
def index(request):
    # Создание контекста для шаблона.
    # Если в шаблоне нужно использовать значения из словаря, то их называют переменными или placeholders и помещают
    # их в {{  }}.
    # Если в шаблоне необходимо выполнить проверку (условие, цикл), то используются теги, то есть ключи и помещают
    # их в {%  %}.
    # Первый ключ это плейсхолдер, а второй это тег.
    context = {
        'title': 'Store',
        'is_promotion': False,
    }
    # Подключаем контекст к файлу index.html. Чтобы получить значение ключа необходимо написать название ключа.
    return render(request, 'products/index.html', context)


# Функция для отображения продуктов.
# category_id может и не передаваться, тогда для отображения всех товаров необходимо установить её в None.
# page=1 делаем чтобы при перенаправлении пользователя на страницу с товарами отображалась первая страница.
def products(request, category_id=None, page_number=1):
    # Если передаётся category_id, то берём все продукты, которые относятся к данной категории.
    # Можно передавать сразу category_id, но если нужно было бы сделать фильтрацию по названию, то необходимо
    # использовать category__name.
    # Иначе если не передаётся, то берём все объекты.
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    # Первым параметром передаётся список продуктов, а вторым сколько товаров нужно отображать на одной странице.
    paginator = Paginator(products, per_page)
    # В зависимости от выбранной страницы будут отображаться нужные товары.
    products_paginator = paginator.page(page_number)
    # Добавляем в контекст данные из повторяющихся блоков в html, чтобы использовать теги в цикле.
    context = {
        'title': 'Store - Каталог',
        # Получаем список всех категорий.
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)


# Контроллер обработчик событий для добавления товаров в корзину.
# Подключаем декоратор доступа.
@login_required
def basket_add(request, product_id):
    # Указываем id продукта, чтобы именно его положить в корзину.
    product = Product.objects.get(id=product_id)
    # Берём все элементы корзины пользователя и определённый продукт, так как если его нет, то мы добавим продукт,
    # а если он есть, то увеличим количество товара на 1.
    baskets = Basket.objects.filter(user=request.user, product=product)

    # Если продукта нет в корзине, то добавляем его в корзину данному пользователю.
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    # Если продукт уже имеется в корзине, то берём его и увеличиваем количество на единицу.
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    # После добавления товара в корзину необходимо возвращать пользователя на ту страницу, на которой он добавлял
    # товар, но это может осуществляться как через каталог, так и через сам профиль.
    # Делается данное перенаправление следующим образом.
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# Контроллер для удаления товаров из корзины. Передаём id корзины.
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
