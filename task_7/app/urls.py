from django.urls import path
from .views import DirectorCreate, DirectorList, DirectorDetail, SchoolCreate, SchoolList, SchoolDetail, school_delete, \
    director_delete

urlpatterns = [
    path('director/create', DirectorCreate.as_view(), name='director_create'),
    path('director/detail/<int:pk>', DirectorDetail.as_view(), name='director_detail'),
    path('director/list', DirectorList.as_view(), name='director_list'),
    path('director/delete/<int:pk>', director_delete, name='director_delete'),

    path('school/create', SchoolCreate.as_view(), name='school_create'),
    path('school/detail/<int:pk>', SchoolDetail.as_view(), name='school_detail'),
    path('school/list', SchoolList.as_view(), name='school_list'),
    path('school/delete/<int:pk>', school_delete, name='school_delete'),
]

from .views import SchoolUpdate, DirectorUpdate

urlpatterns += [
    path('school/update/<int:pk>', SchoolUpdate.as_view(), name='school_update'),
    path('director/update/<int:pk>', DirectorUpdate.as_view(), name='director_update'),
]
