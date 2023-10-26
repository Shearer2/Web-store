from django.contrib import admin
# Импортируем нашу модель пользователей.
from users.models import User
from products.admin import BasketAdmin


# Register your models here.
# Регистрируем модель в админ панели.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    # Добавляем возможность просмотра у определённого пользователя его товаров, если нажать на ник пользователя.
    inlines = (BasketAdmin,)


