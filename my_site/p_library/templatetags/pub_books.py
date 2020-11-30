from django import template

register = template.Library()


@register.filter
def count_books(publisher):
    return publisher.books.count()
