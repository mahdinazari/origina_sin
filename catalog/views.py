from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Book, BookInstance, Author


class Index(generic.TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        books = Book.objects.all().count()
        book_instances = BookInstance.objects.all().count()
        avalable_book_instances = BookInstance.objects\
            .filter(status__exact='a')\
            .all()
        authors = Author.objects.all().count()

        context = super().get_context_data(**kwargs)
        context['books'] = books
        context['book_instances'] = book_instances
        context['avalable_book_instances'] = avalable_book_instances
        context['authors'] = authors
        return context

#def index(request):
#    books = Book.objects.all().count()
#    book_instances = BookInstance.objects.all().count()
#    avalable_book_instances = BookInstance.objects\
#        .filter(status__exact='a')\
#        .all()
#    authors = Author.objects.all().count()
#
#    context = {
#        'books': books,
#        'book_instances': book_instances,
#        'avalable_book_instances': avalable_book_instances,
#        'authors': authors,
#    }

#    return render(request, 'catalog/index.html', context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list'


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list'


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        author_books = Book.objects.filter(author_id=1).all()
        context['author_books'] = author_books
        return context

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    # TODO Fix it
#    login_url = 'accounts/login/'
#    redirect_field_name = 'catalog/'

    def get_queryset(self):
        borrowed_books_list = BookInstance.objects \
            .filter(borrower=self.request.user) \
            .filter(status__exact='o') \
            .order_by('due_back')

        return borrowed_books_list

