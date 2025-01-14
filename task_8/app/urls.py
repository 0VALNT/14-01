from django.urls import path
from .views import DeviceCreate, DeviceList, DeviceDetail, NumberCreate, NumberList, NumberDetail, number_delete, device_delete
urlpatterns = [
    path('device/create', DeviceCreate.as_view(), name='device_create'),
    path('device/detail/<int:pk>', DeviceDetail.as_view(), name='device_detail'),
    path('device/list', DeviceList.as_view(), name='device_list'),
    path('device/delete/<int:pk>', device_delete, name='device_delete'),


    path('number/create', NumberCreate.as_view(), name='number_create'),
    path('number/detail/<int:pk>', NumberDetail.as_view(), name='number_detail'),
    path('number/list', NumberList.as_view(), name='number_list'),
    path('number/delete/<int:pk>', number_delete, name='number_delete'),
]
