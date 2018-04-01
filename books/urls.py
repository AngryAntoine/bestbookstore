from django.urls import path

from .views import (BookCreateView,
                    BookDetailView,
                    BookDeleteView,
                    BookListView,
                    BookUpdateView,
                    RequestListenerView
                    )

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<slug>/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<slug>/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('<slug>/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('request_list/', RequestListenerView.as_view(), name='http_request_list')
]
