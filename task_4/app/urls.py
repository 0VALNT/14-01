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
from .views import OrderUpdate, Order_ItemUpdate, delete_order_item, delete_order

urlpatterns += [
    path('order_item/delete/<int:pk>', delete_order_item, name='order_item_delete'),
    path('order/delete/<int:pk>', delete_order, name='order_delete'),
    path('order/update/<int:pk>', OrderUpdate.as_view(), name='order_update'),
    path('order_item/update/<int:pk>', Order_ItemUpdate.as_view(), name='order_item_update'),
]
