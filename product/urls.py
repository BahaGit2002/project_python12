from django.urls import path

from product.views import ProductListView, ProductListRest, ProductDetailView, ProductCreateView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('list_rest/', ProductListRest.as_view(), name='list_rest'),
    path('create/', ProductCreateView.as_view(), name='create'),
]
