from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Book, Review, Author


# Create your views here.
def index(request):
    # Book.objects.all().delete()
    # Author.objects.all().delete()
    # Review.objects.all().delete()
    return render(request, 'login_registration/index.html')


def register(request):
    results = User.objects.registerVal(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, 'User created, please login.')

    return redirect('/')


def login(request):
    results = User.objects.loginVal(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        request.session['id'] = results['user'].id
        return redirect('/books')
    return redirect('/')


def logout(request):
    request.session.clear()
    messages.success(request, 'Logged Out')
    return redirect('/')


def books(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    user = User.objects.get(id=request.session.get('id'))
    books = Book.objects.all().order_by('-created_at')[:3]
    reviews = Review.objects.all()
    context = {
        'user': user,
        'books': books,
        'reviews': reviews,
    }
    return render(request, 'belt_review/index.html', context)


def booksAdd(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    user = User.objects.get(id=request.session.get('id'))
    authors = Author.objects.all()
    context = {
        'user': user,
        'authors': authors,
    }
    return render(request, 'belt_review/booksAdd.html', context)


def addBook(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    results = Book.objects.addBookVal(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
            return redirect('/books')
    else:
        messages.success(request, 'Book Successfully Added.')
    return redirect('books/'+str(results['book'].id))


def booksView(request, id):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    book = Book.objects.get(id=id)
    author = book.author.name
    reviews = book.review_set.all()
    context = {
        'book': book,
        'author': author,
        'Reviews': reviews,
    }
    return render(request, 'belt_review/book.html', context)


def userProfile(request, id):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    commented = {'books': []}
    user = User.objects.get(id=id)
    booktests = Book.objects.all()
    for book in booktests:
        if book.review_set.filter(users=User.objects.get(id=id)):
            commented['books'].append(book)
    context = {
        'user': user,
        'books': commented['books'],
    }
    return render(request, 'belt_review/user.html', context)


def addReview(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')

    results = Review.objects.addReview(request.POST)

    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, 'Review Successfully Added.')

    return redirect('/books/' + request.POST['book_id'])


def delReview(request, bookid, id):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')

    Review.objects.get(id=id).delete()

    return redirect('/books/' + str(bookid))