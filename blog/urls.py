from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('article/<int:pk>', views.Detail.as_view(), name='detail'),
]

