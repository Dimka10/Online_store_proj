from django.urls import path

from applications.product.views import ProductListView

urlpatterns = [
    path('products-list/', ProductListView.as_view()),
]