# from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.db.models import CASCADE
from django.db.models import CharField, EmailField, TextField, IntegerField, PositiveSmallIntegerField


class Author(Model):
    name = CharField(max_length=120, null=False,)
    country = CharField(max_length=120, null=True,)
    position = CharField(max_length=250, null=True,)
    email = EmailField(null=True)

    def __str__(self):
        return self.name


class Journal(Model):
    JOURNAL_GRADE_CHOICES = [
        ('RINC', 'RINC'),
        ('WAK', 'WAK'),
        ('SCOPUS', 'SCOPUS'),
        ('WOS', 'WOS'),
    ]
    name = CharField(max_length=120, null=False,)
    country = CharField(max_length=120, null=True,)
    grade = CharField(max_length=6,
                      choices=JOURNAL_GRADE_CHOICES,
                      default='RINC',)

    def __str__(self):
        return f'{self.name} is {self.grade}'


class Article(Model):
    title = CharField(max_length=120)
    description = TextField()
    authors = ManyToManyField('Author')
    journal = ForeignKey('Journal', related_name='journal', on_delete=CASCADE)
    year = PositiveSmallIntegerField()  # Посмотреть валидаторы!!!
    number = PositiveSmallIntegerField()
    volume = PositiveSmallIntegerField()
    pages = CharField(max_length=20)

    def __str__(self):
        return f'{self.title} ({self.year})'
