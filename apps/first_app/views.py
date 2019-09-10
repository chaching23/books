from django.shortcuts import render, redirect
from .models import Books
from .models import Authors

def book(request):
    context={
        "all_books" : Books.objects.all(),
    }

    return render(request,"first_app/index.html", context)

def add_books(request):
    Books.objects.create(title=request.POST["title"], description = request.POST["desc"])
    return redirect("/")


def view_books(request, book_id):
    context = {
        "books" : Books.objects.all(),
        "book" : Books.objects.get(id=book_id),
        "authors" : Authors.objects.all(),
        "author" : Books.objects.get(id=book_id).Authors.all(),

    }
    return render(request,"first_app/index2.html", context, book_id)



def insert_author(request):
    if request.method == 'POST':
        book_id=request.POST["book_id"]
        author_id=request.POST["author_id"]
        Books.objects.get(id=book_id).Authors.add(Authors.objects.get(id=author_id))
    return redirect('/')


