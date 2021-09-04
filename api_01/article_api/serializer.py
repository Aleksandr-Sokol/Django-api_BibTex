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
        journal = validated_data['journal']
        journal_name = journal['name']
        journal_filter = Journal.objects.filter(name=journal_name).first()
        if not journal_filter:
            data_journal = {
                'name': journal_name,
            }
            journal_filter = Journal.objects.create(**data_journal)

        authors = validated_data['authors']
        authors_list = []
        for author in authors:
            author_name = author['name']
            author_filter = Author.objects.filter(name=author_name).first()
            if not author_filter:
                data_author = {
                    'name': author_name,
                }
                author_filter = Author.objects.create(**data_author)
            authors_list.append(author_filter)
        data = {
            'title': validated_data['title'],
            'description': validated_data['description'],
            'journal': journal_filter,
        }
        article = Article.objects.create(**data)
        article.authors.set(authors_list)  # many-to-many можно добавлять только к уже существущим (НЕ при создании)
        article.save()
        return article

    def update(self, instance, validated_data):
        print('start update')
        return instance

