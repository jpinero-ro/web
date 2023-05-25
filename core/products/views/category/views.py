from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.products.forms import CategoryForm
from core.products.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        return context


class CategoryCreate(CreateView):
    model = Category
    template_name = 'category/create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo registro de una Categoria'
        context['action'] = 'add'
        return context


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'category/create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Categoria'
        context['action'] = 'edit'
        return context


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('category_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDelete, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Notificación de eliminación'
        context['url'] = reverse_lazy('category_list')
        return context
