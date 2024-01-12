from django.urls import path
# Импортируем созданное нами представление
from .views import ProductsList, ProductDetail, create_product


urlpatterns = [
   path('', ProductsList.as_view()),
   path('<int:id>', ProductDetail.as_view()),
   path('create/', create_product, name='product_create')
]