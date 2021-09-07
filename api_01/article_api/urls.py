from django.urls import path
from .views import ArticleView, SingleArticleView, AuthorView, SingleAuthorView, JournalView, SingleJournalView, FileUploadView


app_name = "article_api"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', SingleArticleView.as_view()),
    path('author/', AuthorView.as_view()),
    path('author/<int:pk>', SingleAuthorView.as_view()),
    path('journal/', JournalView.as_view()),
    path('journal/<int:pk>', SingleJournalView.as_view()),
    path('upload/', FileUploadView.as_view())
]
