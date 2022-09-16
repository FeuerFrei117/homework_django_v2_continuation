from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminUpdateForm, ProductAdminUpdateForm, \
    ProductAdminCreateForm
from authapp.models import User
from mainapp.mixin import CustomDispatchMixin, BaseClassContextMixin, UserDispatchMixin
from mainapp.models import ProductCategory, Product


class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'admins/admin.html'
    title = 'GeekShop - Admin'

        # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(UserListView, self).get_context_data(**kwargs)
    #     context['title'] = 'GeekShop - Admin'
    #     return context

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(UserListView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     context = {
#         'title': 'GeekShop - Admin',
#     }
#     return render(request, 'admins/admin.html', context)

# Users
class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    # context_object_name = 'users' # переопределение object_list
    template_name = 'admins/admin-users-read.html'
    title = 'GeekShop - Админ | Пользователи'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(UserListView, self).get_context_data(**kwargs)
    #     context['title'] = 'GeekShop - Админ | Пользователи'
    #     return context

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {
#         'title' : 'GeekShop - Админ | Пользователи',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'GeekShop - Админ | Регистрация'

    # def get_context_data(self, **kwargs):
    #     context = super(UserCreateView, self).get_context_data(**kwargs)
    #     context['title'] = 'GeekShop - Админ | Регистрация'
    #     return context
    #
    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(UserCreateView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegisterForm()
#
#     context = {
#         'title': 'GeekShop - Админ | Регистрация',
#         'form': form,
#     }
#     return render(request, 'admins/admin-users-create.html', context)


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'GeekShop - Админ | Обновление'

    # def get_context_data(self, **kwargs):
    #     context = super(UserUpdateView, self).get_context_data(**kwargs)
    #     context['title'] = 'GeekShop - Админ | Обновление'
    #     return context
    #
    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, pk):
#
#     user_select = User.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#
#     context = {
#         'title': 'GeekShop - Админ | Обновление',
#         'user_select' : user_select,
#         'form': form,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)


class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    '''
    метод переопределяет метод post
    активирует и деактивирует пользователя
    ps понимаю, что сделал неправильно, но пока не соображу, как сделать правильно
    (по идее надо переопределять метод def delete, но при его переопеделении ничего не рабоатет.)
    '''
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_active_update(request, pk):
#     if request.method == 'POST':
#         user = User.objects.get(pk=pk)
#         if user.is_active:
#             user.is_active = False
#         else:
#             user.is_active = True
#         user.save()
#
#     return HttpResponseRedirect(reverse('admins:admin_users'))

# Category
class AdminCategoriesListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    title = 'GeekShop - Админ | Категории'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(AdminCategoriesListView, self).get_context_data(**kwargs)
    #     context['title'] = 'GeekShop - Админ | Категории'
    #     return context
    #
    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(AdminCategoriesListView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_categories(request):
#     context = {
#         'title' : 'GeekShop - Админ | Категории',
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request, 'admins/admin-categories-read.html', context)


class AdminCategoriesUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoryAdminUpdateForm
    success_url = reverse_lazy('admins:admin_categories')
    title = 'GeekShop - Админ | Категория - Обновление'

    # def get_context_data(self, **kwargs):
    #     context = super(AdminCategoriesUpdateView, self).get_context_data(**kwargs)
    #     context['title'] = 'GeekShop - Админ | Категория - Обновление'
    #     return context
    #
    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(AdminCategoriesUpdateView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_categories_update(request, pk):
#
#     categories_select = ProductCategory.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = CategoryAdminUpdateForm(data=request.POST, instance=categories_select)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_categories'))
#     else:
#         form = CategoryAdminUpdateForm(instance=categories_select)
#
#     context = {
#         'title' : 'GeekShop - Админ | Категория - Обновление',
#         'categories_select': categories_select,
#         'form': form,
#     }
#     return render(request, 'admins/admin-categories-update-delete.html', context)


class AdminCategoriesActiveUpdateView(UpdateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoryAdminUpdateForm
    success_url = reverse_lazy('admins:admin_categories')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u:u.is_superuser)
# def admin_categories_active_update(request, pk):
#     if request.method == 'POST':
#         categories = ProductCategory.objects.get(pk=pk)
#         if categories.is_active:
#             categories.is_active = False
#         else:
#             categories.is_active = True
#         categories.save()
#
#     return HttpResponseRedirect(reverse('admins:admin_categories'))


class AdminCategoriesCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = CategoryAdminUpdateForm
    success_url = reverse_lazy('admins:admin_categories')
    title = 'GeekShop - Админ | Категория - Создание'


# @user_passes_test(lambda u:u.is_superuser)
# def admin_categories_create(request):
#     if request.method == 'POST':
#         form = CategoryAdminUpdateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_categories'))
#     else:
#         form = CategoryAdminUpdateForm()
#
#     context = {
#         'title': 'GeekShop - Админ | Категория - Создание',
#         'form': form,
#     }
#     return render(request, 'admins/admin-categories-create.html', context)

# Product
class AdminProductsListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-read.html'
    title = 'GeekShop - Админ | Продукты'

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products(request):
#     context = {
#         'title': 'GeekShop - Админ | Продукты',
#         'products': Product.objects.all(),
#     }
#     return render(request, 'admins/admin-product-read.html', context)


class AdminProductsUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = ProductAdminUpdateForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'GeekShop - Админ | Продукты - Обновление'

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_update(request, pk):
#
#     product_select = Product.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = ProductAdminUpdateForm(data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductAdminUpdateForm(instance=product_select)
#
#     context = {
#         'title': 'GeekShop - Админ | Продукты - Обновление',
#         'product_select': product_select,
#         'form': form,
#     }
#     return render(request, 'admins/admin-product-update-delete.html', context)


class AdminProductsActiveUpdateView(UpdateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = ProductAdminUpdateForm
    success_url = reverse_lazy('admins:admin_products')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_active_update(request, pk):
#     if request.method == 'POST':
#         product = Product.objects.get(pk=pk)
#         if product.is_active:
#             product.is_active = False
#         else:
#             product.is_active = True
#         product.save()
#
#     return HttpResponseRedirect(reverse('admins:admin_products'))


class AdminProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'GeekShop - Админ | Продукты - Создание'

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_create(request):
#     if request.method == 'POST':
#         form = ProductAdminCreateForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductAdminCreateForm()
#
#     context = {
#         'title': 'GeekShop - Админ | Продукты - Создание',
#         'form': form,
#     }
#
#     return render(request, 'admins/admin-product-create.html', context)

