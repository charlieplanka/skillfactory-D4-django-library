from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, borrowed_books

app_name = "p_library"
urlpatterns = [
    path("author/create", AuthorEdit.as_view(), name="author_create"),
    path("authors", AuthorList.as_view(), name="authors_list"),
    path("author/create_many", author_create_many, name="author_create_many"),
    path("author_book/create_many", books_authors_create_many, name="author_book_create_many"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
