from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from p_library.models import Book, Publisher


def index(request):
    template = loader.get_template("index.html")
    books = Book.objects.all()
    library_data = {
        "title": "библиотека",
        "books": books
        }
    return HttpResponse(template.render(library_data, request))


def publishers(request):
    template = loader.get_template("publishers_list.html")
    publishers = Publisher.objects.all()
    publishers_data = {"publishers": publishers}
    return HttpResponse(template.render(publishers_data))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')
