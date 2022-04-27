from django.shortcuts import render, redirect
from django.urls import reverse

from books.models import Book


def index_view(request):
    return redirect(reverse('books'))


def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.all()
    for b in book_objects:
        print(b.pub_date)
    context = {
        'books': book_objects
    }
    return render(request, template, context)


def books_pagination_view(request, dt):
    template = 'books/book_by_date.html'
    book_objects = Book.objects.filter(pub_date=dt)
    next_book_obj = Book.objects.order_by('pub_date').filter(pub_date__gt=dt)[:1:1]
    prev_book_obj = Book.objects.order_by('-pub_date').filter(pub_date__lt=dt)[:1:1]
    next = next_book_obj[0] if next_book_obj else None
    prev = prev_book_obj[0] if prev_book_obj else None
    context={
        'books': book_objects,
        'prev_book_obj':prev,
        'next_book_obj': next
    }
    return render(request, template, context)
