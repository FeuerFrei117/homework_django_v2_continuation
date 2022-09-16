from django.urls import path

from mainapp.views import ProductsTemplateView, ProductDetail

app_name = 'mainapp'

urlpatterns = [
    path('', ProductsTemplateView.as_view(), name='products'),
    path('category/<int:list_group>/', ProductsTemplateView.as_view(), name='category'),
    path('page/<int:page>/', ProductsTemplateView.as_view(), name='page'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
]
