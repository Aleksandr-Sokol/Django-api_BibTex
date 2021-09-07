from django.shortcuts import render
from rest_framework import filters, pagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Author, Journal
from .serializer import ArticleSerializer, AuthorSerializer, JournalSerializer, FileUploadSerializer
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
    # pagination_class = PageNumberSetPagination
    permission_classes = [MyPermissions]

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)


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

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)


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

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)



class SingleJournalView(RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [MyPermissions]

# ***
# class FileUploadView(APIView):
#     parser_classes = (FileUploadParser,)
#
#     def put(self, request, filename, format=None):
#         file_obj = request.data['file']
#         # ...
#         print(file_obj)
#         print(filename)
#         # ...
#         return Response(status=204)


# class FileUploadView(APIView):
#
#    def post(self, request):
#        # set 'data' so that you can use 'is_vaid()' and raise exception
#        # if the file fails validation
#        print('request')
#        print(request.FILES)
#        print(request.data)
#        serializer = FileUploadSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        # once validated, grab the file from the request itself
#        file = request.FILES['file']
#        print(file)
#        return Response(status=204)

class FileUploadView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = (MultiPartParser,)
    def post(self, request, format=None):
        # to access files
        print(request.FILES)
        # to access data
        print(request.data)
        return Response({'received data': request.data})

    # def post(self, request):
    #     article = request.data.get('article')
    #     serializer = ArticleSerializer(data=article) # десериализация из json в объект article
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()    # сохранение в базу данных
    #     return Response({текст})
