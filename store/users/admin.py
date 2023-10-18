from django.contrib import admin
# Импортируем нашу модель пользователей.
from users.models import User

# Register your models here.
# Регистрируем модель в админ панели.
admin.site.register(User)
