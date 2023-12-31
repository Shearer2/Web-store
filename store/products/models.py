from django.db import models

from users.models import User


# Create your models here.
# Модели это таблицы в базе данных.
# Чтобы python понимал, что мы работаем с базой данных и хотим вносить в неё изменения, необходимо дочерний класс
# наследовать от базового класса Model. Id создаётся по умолчанию через класс Model.
# Если необходимо какое-то другое поле сделать primary_key, то достаточно в скобках просто указать данный параметр со
# значением True.
class ProductCategory(models.Model):
    # Для создания столбца в нашей таблице необходимо через models указать тип значений и длину в символах.
    # Чтобы категории нельзя было создать с одинаковым названием указывается unique со значением True.
    name = models.CharField(max_length=128)
    # CharField - это определённая строка с определённым количеством символов, а TextField - это может быть большой
    # текст. Чтобы показать, что данное поле является не обязательным для заполнения передаём в него два аргумента.
    description = models.TextField(null=True, blank=True)

    # Делаем отображение названия класса в админ-панели на русском языке.
    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    # Используем магический метод str, чтобы при выводе в консоли или в терминале изменение у экземпляра класса можно
    # было получить название.
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    # Для работы с ценами используется тип данных DecimalField. max_digits - это максимальное количество цифр, которые
    # могут быть до запятой. decimal_places - это количество цифр после запятой.
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # Количество товаров на складе. Будем использовать PositiveIntegerField, так как у нас не может быть отрицательное
    # значение. По умолчанию используется 0 товаров на складе, передаём это в параметр default.
    quantity = models.PositiveIntegerField(default=0)
    # При загрузке изображения оно должно куда-то сохраняться, для этого указываем поле upload_to и папку для
    # сохранения.
    image = models.ImageField(upload_to='products_images')
    # При помощи ForeignKey мы связываем наш класс с моделью ProductCategory через поле to.
    # on_delete - указывает как именно удалять, есть каскадное, защищённое и удаление по умолчанию.
    # Если нужно удалить какую-нибудь категорию, то каскадное удаление удалит все товары, которые хранились в данной
    # категории, поэтому обычно используют PROTECT удаление, то есть категорию невозможно будет удалить, пока не будут
    # удалены все продукты принадлежащие данной категории. Если нужно использовать SET_DEFAULT, то в параметр default
    # нужно вписать любое значение, которое будет использоваться при удалении по умолчанию.
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    # Делаем отображение названия класса в админ-панели на русском языке.
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    # Чтобы поменять отображение продуктов в админ панели необходимо переопределить магический метод str.
    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'


# Можно создать свой собственный QuerySet но с добавлением своих методов. Используем его для подсчёта суммы и
# количества всех товаров.
class BasketQuerySet(models.QuerySet):

    # Метод для подсчёта общей суммы товаров.
    def total_sum(self):
        return sum(basket.sum() for basket in self.filter())

    # Метод для подсчёта количества всех товаров.
    def total_quantity(self):
        return sum(basket.quantity for basket in self)


# Создаём таблицу с корзиной.
class Basket(models.Model):
    # Указываем пользователя, наследуясь от класса User.
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # Указываем продукты, наследуясь от класса Product.
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    # Указываем количество предметов, который пользователь решил купить.
    quantity = models.PositiveSmallIntegerField(default=0)
    # При помощи параметра auto_now_add новые переменные будут сами сохраняться.
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    # Добавляем метод для подсчёта суммы товара.
    def sum(self):
        return self.product.price * self.quantity
