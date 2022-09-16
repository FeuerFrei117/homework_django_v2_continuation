from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
import json
import os

from django.views.generic import DetailView, TemplateView, ListView

from mainapp.mixin import BaseClassContextMixin
from mainapp.models import ProductCategory, Product


class IndexTemplateView(TemplateView, BaseClassContextMixin):
    template_name = 'mainapp/index.html'
    title = 'GeekShop'

# def index(request):
#     context = {
#         'title': 'GeekShop',
#     }
#     return render(request, 'mainapp/index.html', context)


class ProductsTemplateView(ListView, BaseClassContextMixin):
    template_name = 'mainapp/products.html'
    title = 'GeekShop | Каталог'
    model = Product
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsTemplateView, self).get_context_data(**kwargs)
        context['list_groups'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        super(ProductsTemplateView, self).get_queryset()
        if self.kwargs.__len__() == 0:
            queryset = Product.objects.filter(is_active=True, category__is_active=True)
        else:
            queryset = Product.objects.filter(category_id=self.kwargs['list_group'], is_active=True, category__is_active=True)
        return queryset

# def products(request, id_category=None, page=1):
#     with open(os.getcwd() + '\\mainapp\\fixtures\\products.json', 'r', encoding='utf-8') as f:
#         templates = json.load(f)
#
#     if id_category:
#         clothes = Product.objects.filter(category_id=id_category, is_active=True, category__is_active=True)
#     else:
#         clothes = Product.objects.filter(is_active=True, category__is_active=True)
#
#     paginator = Paginator(clothes, per_page=3)
#
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#
#     context = {
#         'title': 'GeekShop | Каталог',
#         'list_groups': ProductCategory.objects.all(),
#         'clothes': products_paginator,
#     }
#     return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'
    # context_object_name = 'product'

    """Если работаем с классами, код ниже можно не писать"""
    # def get_context_data(self,**kwargs):
    #     """Добавляем список категорий для вывода сайдбара с категориями на странице каталога"""
    #     context = super(ProductDetail, self).get_context_data(**kwargs)
    #     product = self.get_object()
    #     context['product'] = product
    #     return context




















