from django.shortcuts import render
from django.views import generic

from .models import Article


class Index(generic.ListView):
    model = Article
    template_name = 'blog/index.html'


class Detail(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'

