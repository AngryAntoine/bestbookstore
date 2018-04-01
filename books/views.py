from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import (CreateView, DeleteView, UpdateView)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import BookCreateForm
from .models import (Book,
                     RequestListener
                     )

from .utils import request_string


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        queryset = Book.objects.filter(active=True).order_by('publish_date')
        order_by = self.request.GET.get('order_by', '')
        if order_by:
            queryset = queryset.order_by('-publish_date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data()
        abs_uri = self.request.build_absolute_uri()
        if abs_uri: request_string(RequestListener, abs_uri)
        return context


class BookCreateView(LoginRequiredMixin, CreateView):
    form_class = BookCreateForm
    template_name = 'forms/form.html'
    login_url = reverse_lazy('admin:index')  # can be set in main settings file as LOGIN_URL, but view itself can override it
    # success_url = reverse_lazy('books:book_list')  # if there's no get_absolute_url method on model

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data()
        context['head_title'] = 'Create Book'
        abs_uri = self.request.build_absolute_uri()
        if abs_uri: request_string(RequestListener, abs_uri)
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data()
        context['head_title'] = 'Create Book'
        abs_uri = self.request.build_absolute_uri()
        if abs_uri: request_string(RequestListener, abs_uri)
        return context


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'forms/form.html'
    context_object_name = 'book'
    login_url = reverse_lazy('admin:index')

    def get_context_data(self, **kwargs):
        context = super(BookUpdateView, self).get_context_data()
        context['head_title'] = 'Update Book'
        abs_uri = self.request.build_absolute_uri()
        if abs_uri: request_string(RequestListener, abs_uri)
        return context


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'forms/form.html'
    success_url = reverse_lazy('books:book_list')
    login_url = reverse_lazy('admin:index')

    def get_context_data(self, **kwargs):
        context = super(BookDeleteView, self).get_context_data()
        context['head_title'] = 'Delete Book'
        abs_uri = self.request.build_absolute_uri()
        if abs_uri: request_string(RequestListener, abs_uri)
        return context


class RequestListenerView(ListView):
    model = RequestListener
    template_name = 'books/http_request_list.html'
    context_object_name = 'request_list'

    def get_queryset(self):
        queryset = RequestListener.objects.all().order_by('-pk')[:10]
        return queryset

    def get_context_data(self, **kwargs):
        context = super(RequestListenerView, self).get_context_data()
        context['head_title'] = 'Request List'
        abs_uri = self.request.build_absolute_uri()
        if abs_uri: request_string(RequestListener, abs_uri)
        return context
