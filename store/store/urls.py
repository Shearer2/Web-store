"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Импортируем модули необходимые для работы с изображениями.
from django.conf.urls.static import static
# Именно данным образом необходимо подключать модуль с настройками, так как таким способом подтягиваются все настройки
# проекта. А если просто импортировать настройки из нашего проекта, то возьмутся только внешние настройки.
from django.conf import settings

from products.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # Добавляем главную страницу, оставив пустые кавычки.
    path('', index, name='index'),
    # Добавляем страницу с продуктами.
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
]

# Чтобы изображения отображались локально делаем следующую проверку.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
