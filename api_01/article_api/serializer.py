from rest_framework import serializers
from .models import Article, Author, Journal


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'country', 'position')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'name', 'country', 'grade')


class ArticleSerializer(serializers.ModelSerializer):
    journal = JournalSerializer(many=False, read_only=False)
    authors = AuthorSerializer(many=True, read_only=False)

    class Meta:
        model = Article
        fields = ('id', 'title', 'authors', 'description', 'year', 'journal', 'number', 'volume', 'pages', 'doi')

    def create(self, validated_data):
        validated_data_copy = validated_data.copy()
        journal = validated_data_copy.pop('journal')
        journal_filter = Journal.objects.filter(name=journal['name']).first()
        if not journal_filter:
            journal_filter = Journal.objects.create(**journal)

        authors = validated_data_copy.pop('authors')
        authors_list = []
        for author in authors:
            author_name = author['name']
            author_filter = Author.objects.filter(name=author_name).first()
            if not author_filter:
                author_filter = Author.objects.create(**author)
            authors_list.append(author_filter)

        validated_data_copy['journal'] = journal_filter
        article = Article.objects.create(**validated_data_copy)
        article.authors.set(authors_list)  # many-to-many можно добавлять только к уже существущим (НЕ при создании)
        article.file = None
        article.save()
        return article

    def update(self, instance, validated_data):
        print('start update')
        return instance


# class FileUploadSerializer(serializers.Serializer):
#     # I set use_url to False so I don't need to pass file
#     # through the url itself - defaults to True if you need it
#     file = serializers.FileField(use_url=False)
