from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from store.models import Cart, Order
from django.shortcuts import render
from store.models import SearchForm
from store.models import Promotion
from django.http import JsonResponse
from store.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, )
    discounted_price = product.price

    if product.promotion:
        discount_percentage = product.promotion.discount
        discounted_price = product.price - (product.price * (discount_percentage / 100))
    else:
        discounted_price = product.price

    return render(request, 'store/detail.html', context={"product": product, 'discounted_price': discounted_price})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,ordered=False, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'store/cart.html', context={"orders": cart.orders.all()})

def delete_cart(request):

    if cart := request.user.cart:
        cart.delete()

    return redirect('index')

def search(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'form': form, 'results': results})

def promotion_list(request):
    active_promotions = Promotion.objects.filter(end_date__lte=timezone.now().date())

def products_api(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
    return JsonResponse(data, safe=False)
