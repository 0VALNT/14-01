from django.urls import path
from .views import LibraryCreate, LibraryList, LibraryDetail, BookCreate, BookList, BookDetail

urlpatterns = [
    path('library/create', LibraryCreate.as_view(), name='library_create'),
    path('library/detail/<int:pk>', LibraryDetail.as_view(), name='library_detail'),
    path('library/list', LibraryList.as_view(), name='library_list'),

    path('book/create', BookCreate.as_view(), name='book_create'),
    path('book/detail/<int:pk>', BookDetail.as_view(), name='book_detail'),
    path('book/list', BookList.as_view(), name='book_list'),
]

from .views import BookUpdate, LibraryUpdate, delete_library, delete_book

urlpatterns += [
    path('library/delete/<int:pk>', delete_library, name='library_delete'),
    path('book/delete/<int:pk>', delete_book, name='book_delete'),
    path('book/update/<int:pk>', BookUpdate.as_view(), name='book_update'),
    path('library/update/<int:pk>', LibraryUpdate.as_view(), name='library_update'),
]
