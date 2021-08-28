from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, get_object_or_404
from .models import Article, Author
from .serializer import ArticleSerializer


class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
