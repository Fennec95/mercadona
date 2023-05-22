from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, add_to_cart, cart, delete_cart, search, products_api
from accounts.views import signup, logout_user, login_user
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('cart/', cart, name='cart'),
    path('cart/delete', delete_cart, name='delete-cart'),
    path('search/', search, name='search'),
    path('product/<str:slug>/', product_detail, name="product"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
    path('api/products', products_api, name='products_api'),
    path('favicon.ico', RedirectView.as_view(url='/favicon.ico')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)