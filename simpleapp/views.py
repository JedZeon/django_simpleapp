# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime


# from pprint import pprint


class ProductsList(ListView):
    model = Product  # Указываем модель, объекты которой мы будем выводить
    ordering = 'name'  # Поле, которое будет использоваться для сортировки объектов
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # context['next_sale'] = None
        context['next_sale'] = "Распродажа в среду!" # Произвольное значение произвольной переменной

        # pprint(context)

        return context


class ProductDetail(DetailView):
    model = Product                 # Модель всё та же, но мы хотим получать информацию по отдельному товару
    template_name = 'product.html'  # Используем другой шаблон — product.html
    context_object_name = 'product' # Название объекта, в котором будет выбранный пользователем продукт
    pk_url_kwarg = 'id'             # Просто чтобы в urls, указать не pk а id
