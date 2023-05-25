import os
from django.db import models
from config.settings import STATIC_URL, MEDIA_URL


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-name']


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['-name']


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    cat = models.ForeignKey(Category, verbose_name='Categoria', null=True, blank=True, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, verbose_name='Marca', null=True, blank=True, on_delete=models.PROTECT)
    cost = models.DecimalField(decimal_places=2, max_digits=9, default=0.00, verbose_name='Costo')
    price = models.DecimalField(decimal_places=2, max_digits=9, default=0.00, verbose_name='Precio')
    image = models.ImageField(upload_to='product/%Y/%m/%d', verbose_name='Imagen', null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_cat(self):
        if self.cat:
            return self.cat.name
        return None

    def get_image(self):
        if self.image:
            return "{0}{1}".format(MEDIA_URL, self.image)
        return "{0}{1}".format(STATIC_URL, 'img/default/empty.png')

    def cost_format(self):
        return format(self.cost, '.2f')

    def price_format(self):
        return format(self.price, '.2f')

    def delete(self, using=None, keep_parents=False):
        try:
            os.remove(self.image.path)
        except:
            pass
        super(Product, self).delete()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-name']
