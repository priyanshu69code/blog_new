from django.urls import path, include
from .views import HomeView, ArticleView, CreatePost, UpdatePost, DeletePost, CategoryView, LikeView

urlpatterns = [
    # path("",views.home,name="home"),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleView.as_view(), name="article-detail"),
    path("create/", CreatePost.as_view(), name="create"),
    path("article/edit/<int:pk>", UpdatePost.as_view(), name="update"),
    path("article/delete/<int:pk>", DeletePost.as_view(), name="delete"),
    path("category-detail/<int:pk>",
         CategoryView.as_view(), name="category-detail"),
    path("like/<int:pk>", LikeView, name="like_post")
]
