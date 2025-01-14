from django.urls import path
from .views import OrderCreate, OrderList, OrderDetail, Order_ItemCreate, Order_ItemList, Order_ItemDetail
urlpatterns = [
    path('order/create', OrderCreate.as_view(), name='order_create'),
    path('order/detail/<int:pk>', OrderDetail.as_view(), name='order_detail'),
    path('order/list', OrderList.as_view(), name='order_list'),

    path('order_item/create', Order_ItemCreate.as_view(), name='order_item_create'),
    path('order_item/detail/<int:pk>', Order_ItemDetail.as_view(), name='order_item_detail'),
    path('order_item/list', Order_ItemList.as_view(), name='order_item_list'),
]
