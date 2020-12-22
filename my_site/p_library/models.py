from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Friend(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    publisher = models.ForeignKey(Publisher, related_name="books", on_delete=models.SET_NULL, null=True, blank=True)
    borrower = models.ForeignKey(Friend, related_name="borrowed_books", on_delete=models.SET_NULL, null=True, blank=True)
    cover = models.ImageField(upload_to='book_covers', blank=True)

    def __str__(self):
        return self.title

