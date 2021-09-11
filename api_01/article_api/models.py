# from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from django.db.models import CASCADE, BooleanField
from django.db.models import CharField, EmailField, TextField, PositiveSmallIntegerField, DateField

from .validatos import validateRussianSymbols


class PfdfFile(Model):
    name = CharField(max_length=120, null=True)

class Author(Model):
    name = CharField(max_length=120, null=False, unique=True)
    country = CharField(max_length=120, null=True,)
    position = CharField(max_length=250, null=True,)
    email = EmailField(null=True, unique=True)

    def __str__(self):
        return self.name


class Journal(Model):
    JOURNAL_GRADE_CHOICES = [
        ('RINC', 'RINC'),
        ('WAK', 'WAK'),
        ('SCOPUS', 'SCOPUS'),
        ('WOS', 'WOS'),
    ]
    name = CharField(max_length=120, null=False, unique=True)
    country = CharField(max_length=120, null=True,)
    grade = CharField(max_length=6,
                      choices=JOURNAL_GRADE_CHOICES,
                      default='RINC',)

    def __str__(self):
        return f'{self.name} is {self.grade}'


class Article(Model):
    language = CharField(max_length=20, null=True)
    bibTexId = CharField(max_length=30, null=True, unique=True)
    title = CharField(max_length=120, null=False)
    description = TextField(null=True)
    authors = ManyToManyField('Author')
    journal = ForeignKey('Journal', related_name='journal', on_delete=CASCADE)
    file = ForeignKey('PfdfFile', related_name='file', on_delete=CASCADE)  # заготовка для хранения файла
    year = DateField()  # datetime.date(1997, 10, 19)
    number = PositiveSmallIntegerField(null=True)
    volume = PositiveSmallIntegerField(null=True)
    pages = CharField(max_length=20, null=True)
    doi = CharField(max_length=50, validators=[validateRussianSymbols], null=True, unique=True)

    class Meta:
        unique_together = 'title', 'journal'

    def __str__(self):
        return f'{self.title} ({self.year})'
