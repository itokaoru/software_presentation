from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Avg
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from .consts import ITEM_PER_PAGE
from .models import Book, Review


class ListBookView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/book_list.html'
    paginate_by = ITEM_PER_PAGE


class DetailBookView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'


class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book/book_create.html'
    fields = ('title', 'text', 'thumbnail')
    success_url = reverse_lazy('list-book')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteBookView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('list-book')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj


class UpdateBookView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'book/book_update.html'
    fields = ('title', 'text', 'thumbnail')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.id})

class MenuView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'soft/menu_list.html'

class MapView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'soft/map_detail.html'


def index_view(request):
    object_list = Book.objects.order_by('-id')
    ranking_list = Book.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
    paginator = Paginator(ranking_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)
    return render(
        request,
        'book/index.html',
        {
            'object_list': object_list,
            'ranking_list': ranking_list,
            'page_obj': page_obj,
        }
    )


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'book/review_form.html'
    fields = ('book', 'title', 'text', 'rate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.book.id})
