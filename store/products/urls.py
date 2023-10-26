from django.urls import path

from products.views import products, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    # Чтобы остался тот же самый путь, что и был products, необходимо оставить пустые кавычки. Если что-то добавить,
    # то и после products добавится.
    path('', products, name='index'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_number>', products, name='paginator'),
    # Если в контроллере мы передаём определённую переменную, то здесь её тоже необходимо указать вместо с типом.
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    # Подключаем контроллер для удаления корзины.
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
