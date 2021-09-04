from django.shortcuts import render
from rest_framework import filters, pagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, get_object_or_404
from .models import Article, Author, Journal
from .serializer import ArticleSerializer, AuthorSerializer, JournalSerializer
from .permissions import MyPermissions

class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    ordering = 'title'


# ****
class ArticleView(ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = PageNumberSetPagination
    permission_classes = [MyPermissions]


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [MyPermissions]



# ***
class AuthorView(ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [MyPermissions]


class SingleAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [MyPermissions]


# ***
class JournalView(ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [MyPermissions]


class SingleJournalView(RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [MyPermissions]
