from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from p_library.models import Book, Publisher, Author
from p_library.forms import AuthorForm, BookForm
from allauth.socialaccount.models import SocialAccount


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("p_library:author_list")
    template_name = "author_edit.html"


class AuthorList(ListView):
    model = Author
    template_name = "authors_list.html"


def library(request):
    template = loader.get_template("index.html")
    books = Book.objects.all()
    library_data = {
        "title": "библиотека",
        "books": books
        }
    if request.user.is_authenticated:
        library_data["username"] = request.user.username
        try:
            library_data['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']
        except SocialAccount.DoesNotExist:
            pass
    return HttpResponse(template.render(library_data, request))


def publishers(request):
    template = loader.get_template("publishers_list.html")
    publishers = Publisher.objects.all()
    publishers_data = {"publishers": publishers}
    return HttpResponse(template.render(publishers_data))


def book_increment(request):
    if request.method == "POST":
        book_id = request.POST["id"]
        if not book_id:
            return redirect("/index/")
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect("/index/")
            book.copy_count += 1
            book.save()
        return redirect("/")
    else:
        return redirect("/")


def book_decrement(request):
    if request.method == "POST":
        book_id = request.POST["id"]
        if not book_id:
            return redirect("/index/")
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect("/index/")
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect("/")
    else:
        return redirect("/")


def add_author(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect("p_library:authors_list")
    else:
        author_form = AuthorForm()
        return render(request, 'add_author.html', {'form': author_form})


def add_book(request):
    if request.method == "POST":
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect("p_library:library")
    else:
        book_form = BookForm()
        return render(request, 'add_book.html', {'form': book_form})


def borrowed_books(request):
    template = loader.get_template("borrowed_books.html")
    borrowed_books = Book.objects.filter(borrower__isnull=False)
    books_data = {"books": borrowed_books}
    return HttpResponse(template.render(books_data))
