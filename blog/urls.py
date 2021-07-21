from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('article/<int:pk>', views.Detail.as_view(), name='detail'),
    path('article/create', views.ArticleCreate.as_view(), name='create'),
    path('category/', views.CategoryIndex.as_view(), name='categry-index'),
    path(
        'category/<int:pk>',
        views.CategoryDetail.as_view(),
        name='category_detail'
    ),
    path('authors/', views.AuthorIndex.as_view(), name='author-index'),
    path(
        'authors/<slug:username>',
        views.AuthorDetail.as_view(),
        name='author-detail',
    ),
]

