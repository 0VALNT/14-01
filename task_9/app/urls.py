from django.urls import path
from .views import AthleteCreate, AthleteList, AthleteDetail, RecordCreate, RecordList, RecordDetail, record_delete, athlete_delete
urlpatterns = [
    path('athlete/create', AthleteCreate.as_view(), name='athlete_create'),
    path('athlete/detail/<int:pk>', AthleteDetail.as_view(), name='athlete_detail'),
    path('athlete/list', AthleteList.as_view(), name='athlete_list'),
    path('athlete/delete/<int:pk>', athlete_delete, name='athlete_delete'),


    path('record/create', RecordCreate.as_view(), name='record_create'),
    path('record/detail/<int:pk>', RecordDetail.as_view(), name='record_detail'),
    path('record/list', RecordList.as_view(), name='record_list'),
    path('record/delete/<int:pk>', record_delete, name='record_delete'),
]
