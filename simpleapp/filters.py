from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter
# ModelChoiceFilter - единичный выбор
# ModelMultipleChoiceFilter - множественный выбор
from .models import Product, Material


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(FilterSet):
    material = ModelMultipleChoiceFilter(
        field_name='productmaterial__material',
        queryset=Material.objects.all(),
        label='Материал',
        # empty_label='любой',
        conjoined=False  # Все выбранные материалы должны присутсвовать в продукте
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Product
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            'productmaterial__material': ['exact'],
            # поиск по названию
            'name': ['icontains'],
            # количество товаров должно быть больше или равно
            'quantity': ['gt'],
            'price': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ],
        }
