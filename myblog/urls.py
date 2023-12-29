from django.urls import path, include
from .views import HomeView, ArticleView, CreatePost

urlpatterns = [
    # path("",views.home,name="home"),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleView.as_view(), name="article-detail"),
    path("create/", CreatePost.as_view(), name="create")
]
