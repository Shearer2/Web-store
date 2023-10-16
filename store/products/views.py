from django.shortcuts import render


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
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': 23725,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
            },
            {
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390,
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
            }
        ]
    }
    return render(request, 'products/products.html', context)
