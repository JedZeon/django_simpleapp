from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductForm
from .models import Product
from .filters import ProductFilter


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2  # вот так мы можем указать количество записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict,
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ProductFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_sale'] = "Распродажа в среду!"  # Произвольное значение произвольной переменной

        # Добавляем в контекст объект фильтрации
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product  # Модель всё та же, но мы хотим получать информацию по отдельному товару
    template_name = 'product.html'  # Используем другой шаблон — product.html
    context_object_name = 'product'  # Название объекта, в котором будет выбранный пользователем продукт
    pk_url_kwarg = 'id'  # Просто чтобы в urls, указать не pk а id


# Добавляем новое представление для создания товаров.
class ProductCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ProductForm
    # модель товаров
    model = Product
    # и новый шаблон, в котором используется форма.
    template_name = 'product_edit.html'


# Добавляем представление для изменения товара.
class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


# Представление удаляющее товар.
class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    # Куда перенаправить пользователя после удаления
    success_url = reverse_lazy('product_list')