from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.products.forms import BrandForm
from core.products.models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'brand/list.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BrandListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Marcas'
        return context


class BrandCreate(CreateView):
    model = Brand
    template_name = 'brand/create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BrandCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo registro de una marca'
        context['action'] = 'add'
        return context


class BrandUpdate(UpdateView):
    model = Brand
    template_name = 'brand/create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BrandUpdate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una marca'
        context['action'] = 'edit'
        return context


class BrandDelete(DeleteView):
    model = Brand
    template_name = 'brand/delete.html'
    success_url = reverse_lazy('brand_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BrandDelete, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Notificación de eliminación'
        context['url'] = reverse_lazy('brand_list')
        return context
