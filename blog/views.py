from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Article, Category


class Index(LoginRequiredMixin, generic.ListView):
    template_name = 'blog/index.html'
    paginate_by = 3

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Article.objects.published()

        else:
            queryset = Article.objects.published() \
                .filter(author=self.request.user) \
                .all()

        return queryset


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

class AuthorIndex(generic.ListView):
    model = User
    template_name = 'blog/author_list.html'


class AuthorDetail(generic.ListView):
    paginate_by = 5
    template_name = 'blog/author_detail.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.all()

    def get_context_data(self, **kwargs):
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context


class ArticleCreate(LoginRequiredMixin, generic.CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    fields = [
        'title',
        'slug',
        'description',
        'thumbnail',
        'publish',
        'status',
        'category',
        'author'
    ]

