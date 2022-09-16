from django.urls import path

from admins.views import IndexTemplateView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
    AdminCategoriesListView, AdminCategoriesUpdateView, AdminCategoriesActiveUpdateView , AdminCategoriesCreateView, \
    AdminProductsListView, AdminProductsUpdateView, AdminProductsActiveUpdateView, AdminProductCreateView

app_name = 'admins'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),

    path('users/',UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_active_update'),

    path('categories/', AdminCategoriesListView.as_view(), name='admin_categories'),
    path('categories-create/', AdminCategoriesCreateView.as_view(), name='admin_categories_create'),
    path('categories-update/<int:pk>', AdminCategoriesUpdateView.as_view(), name='admin_categories_update'),
    path('categories-delete/<int:pk>', AdminCategoriesActiveUpdateView.as_view(), name='admin_categories_active_update'),

    path('products/', AdminProductsListView.as_view(), name='admin_products'),
    path('products-create/', AdminProductCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>', AdminProductsUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>', AdminProductsActiveUpdateView.as_view(), name='admin_products_active_update'),
]
