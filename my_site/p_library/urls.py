from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import AuthorList, add_book, add_author, publishers, borrowed_books, library, book_increment, book_decrement

app_name = "p_library"
urlpatterns = [
    path("authors", AuthorList.as_view(), name="authors_list"),
    path("add_book", add_book, name="add_book"),
    path("add_author", add_author, name="add_author"),
    path("publishers", publishers, name="publishers"),
    path("borrowed_books", borrowed_books, name="borrowed_books"),
    path("", library, name="library"),
    path("library/book_increment/", book_increment),
    path("library/book_decrement/", book_decrement),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
