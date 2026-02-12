from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Book(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.CharField(max_length=100)
    genre = models.ManyToManyField('Genre', related_name='books')
    publication_date = models.DateField()
    length = models.PositiveIntegerField(help_text="Length in pages")
    isbn = models.CharField(max_length=13, unique=True)
    summary = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f"{self.title} by {self.author}"


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"