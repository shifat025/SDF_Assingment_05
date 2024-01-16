from django.shortcuts import render
from Book.models import Books,Book_category
from django.views.generic import DetailView
from Borrowbook.forms import ReviewForm
from Borrowbook.views import borrow
from Borrowbook.models import Borrowedbook
from django.http import HttpResponseForbidden

def home(request, book_slug = None):
    data = Books.objects.all()
    if book_slug is not None:
        books = Book_category.objects.get(slug = book_slug)
        data = Books.objects.filter(book_type = books)
    book = Book_category.objects.all()
    return render(request, 'home.html', {'data': data, 'book': book})

class Details(DetailView):
    model = Books
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'
    context_object_name = 'details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_model = self.object

        # Check if the user has bought the specific book
        has_bought_book = Borrowedbook.objects.filter(user=self.request.user, books=book_model).exists()

        if has_bought_book:
            reviews = book_model.review_set.all()
            review_form = ReviewForm()
        else:
            reviews = None
            review_form = None

        context['reviews'] = reviews
        context['review_form'] = review_form
        context['has_bought_book'] = has_bought_book

        return context

    def post(self, request, *args, **kwargs):
        book_model = self.get_object()

        # Check if the user has bought the specific book
        if not Borrowedbook.objects.filter(user=request.user, books=book_model).exists():
            return HttpResponseForbidden("You can only review books you have bought.")

        review_form = ReviewForm(data=self.request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = book_model
            new_review.user = self.request.user
            new_review.save()
        return self.get(request, *args, **kwargs)