from django.forms import *
from .models import *


class BrandForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
        }

    id = IntegerField(widget=HiddenInput(attrs={'id': 'id'}), initial=0)


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'description': Textarea(attrs={'placeholder': 'Ingrese una descripción', 'rows': 3, 'cols': 3}),
        }

    id = IntegerField(widget=HiddenInput(attrs={'id': 'id'}), initial=0)


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'cat': Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10'}),
            'brand': Select(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true', 'data-size': '10'}),
        }

    id = IntegerField(widget=HiddenInput(attrs={'id': 'id'}), initial=0)
