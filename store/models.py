from django.db import models
from django.urls import reverse
from datetime import date
from django import forms
from django.utils import timezone
from shop.settings import AUTH_USER_MODEL


class Promotion(models.Model):
    name = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=15, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def is_active(self):
        current_date = timezone.now().date()
        return self.start_date <= current_date <= self.end_date

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(max_length=128)
    price = models.DecimalField(default=0.0, max_digits=15, decimal_places=2)
    promotion = models.ForeignKey('Promotion', on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.stock})"

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()
        super().delete(*args, **kwargs)


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Rechercher...'}))


class Category(models.Model):
    name = models.CharField(max_length=100)
    # Ajoutez d'autres champs spécifiques à votre modèle Category si nécessaire

    def __str__(self):
        return self.name