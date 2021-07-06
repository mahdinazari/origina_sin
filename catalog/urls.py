from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'catalog'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('authors', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]
