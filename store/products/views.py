from django.shortcuts import render

from products.models import ProductCategory, Product


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
def products(request):
    # Добавляем в контекст данные из повторяющихся блоков в html, чтобы использовать теги в цикле.
    context = {
        'title': 'Store - Каталог',
        # Получаем список всех категорий.
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
