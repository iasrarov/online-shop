from django.urls import path
from . views import (
    cart,
    checkout,
    store,
    updateItem,
    processOrder,
    loginPage,
    registerPage,
)

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('store/', store, name='store'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
]