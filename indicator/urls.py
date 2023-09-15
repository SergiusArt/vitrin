from django.urls import path

from indicator.apps import IndicatorConfig
from indicator.views import index

# Конфигурационное имя приложения
app_name = IndicatorConfig.name

# Ссылки на страницы приложения Catalog
urlpatterns = [
    path('', index, name='index'),
]