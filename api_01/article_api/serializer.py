from rest_framework import serializers
from .models import Article, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'email')


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=False)
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author')