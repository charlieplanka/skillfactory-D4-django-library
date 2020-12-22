from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('title', 'author_full_name', 'publisher')
    fields = ('ISBN', 'title', 'description', 'author', 'cover', 'publisher', 'year_release', 'price', 'copy_count', 'borrower')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


class BookInlineAdmin(admin.StackedInline):
    model = Book
    list_display = ('title', 'author')

    def has_change_permission(self, request, obj=None):
        return False


class BorrowedBookInlineAdmin(BookInlineAdmin):
    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInlineAdmin]


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    inlines = [BorrowedBookInlineAdmin]
