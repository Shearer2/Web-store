from django.db import models
# Импортируем структуру админ панели.
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # Добавляем поле для работы с изображениями, расширяя родительский класс, указываем, что данное поле не обязательно
    # для заполнения.
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

