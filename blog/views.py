from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Article, Category


class Index(generic.ListView):
    queryset = Article.objects.published()
    template_name = 'blog/index.html'
    paginate_by = 3


class Detail(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'


class CategoryIndex(generic.ListView):
    model = Category
    template_name = 'blog/category_index.html'


class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'blog/category_detail.html'

#    def get_object(self):
#        return self.model.objects.all()
#
#    def get_queryset(self):
#        global category
#        pk = self.kwargs.get('pk')
#        category = get_object_or_404(Category, pk=pk, status=True)
#        return category.articles.all()
#
#    def get_context_data(self, **kwargs):
#        pk = self.kwargs.get('pk')
#        category = get_object_or_404(Category, pk=pk, status=True)
#        context = super().get_context_data(**kwargs)
#        context['category'] = category
#        return context
#
