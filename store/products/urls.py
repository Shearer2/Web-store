from django.urls import path

from products.views import products

app_name = 'products'

urlpatterns = [
    # Чтобы остался тот же самый путь, что и был products, необходимо оставить пустые кавычки. Если что-то добавить,
    # то и после products добавится.
    path('', products, name='index')
]
