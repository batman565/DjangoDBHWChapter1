from django.shortcuts import render
from books.models import Book
from django.utils.dateparse import parse_date


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('-pub_date')
    context = {
        'books': books
    }
    return render(request, template, context)


def books_pub_date(request, pubdate):
    template = 'books/books_pub_date.html'
    current_date = parse_date(pubdate)
    books = Book.objects.filter(pub_date=current_date).order_by('pub_date')
    
    prev_date = Book.objects.filter(
        pub_date__lt=current_date
    ).order_by('-pub_date').values_list('pub_date', flat=True).first()
    
    next_date = Book.objects.filter(
        pub_date__gt=current_date
    ).order_by('pub_date').values_list('pub_date', flat=True).first()

    context = {
        'books': books,
        'current_date': current_date,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    return render(request, template, context)


def add_book():
    book = Book(name = 'Сияние', author = 'Стивен Кинг', pub_date = '2018-09-10')
    book.save()
    book1 = Book(name = '1984', author = 'Джордж Оруэл', pub_date = '2015-03-11')
    book1.save()