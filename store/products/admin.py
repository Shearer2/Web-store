from django.contrib import admin
# Импортируем наши модели.
from products.models import ProductCategory, Product

# Register your models here.
# Регистрируем модели в админ панели.
admin.site.register(Product)
admin.site.register(ProductCategory)
