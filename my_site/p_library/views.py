from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from p_library.models import Book, Publisher, Author
from p_library.forms import AuthorForm, BookForm


class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy("p_library:author_list")
    template_name = "author_edit.html"


class AuthorList(ListView):
    model = Author
    template_name = "authors_list.html"


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


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})


def books_authors_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)
    BookFormSet = formset_factory(BookForm, extra=2)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
        request,
        'manage_books_authors.html',
      		{
                    'author_formset': author_formset,
                    'book_formset': book_formset,
            }
    )
