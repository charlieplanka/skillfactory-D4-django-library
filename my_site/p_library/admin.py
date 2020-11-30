from django.contrib import admin
from p_library.models import Book, Author, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('title', 'author_full_name', 'publisher')
    fields = ('ISBN', 'title', 'description', 'author', 'publisher', 'year_release', 'price', 'copy_count')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


class BookInlineAdmin(admin.StackedInline):
    model = Book
    list_display = ('title', 'author')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInlineAdmin]
