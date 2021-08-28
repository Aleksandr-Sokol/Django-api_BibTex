from rest_framework import serializers
from .models import Article, Author, Journal


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'email', 'country', 'position')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('name', 'country', 'grade')


class ArticleSerializer(serializers.ModelSerializer):
    journal = JournalSerializer(many=False, read_only=False)
    authors = AuthorSerializer(many=True, read_only=False)
    class Meta:
        model = Article
        fields = ('id', 'title', 'authors', 'description', 'year', 'journal', 'number', 'volume', 'pages')
