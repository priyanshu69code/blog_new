from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.
# def home(request):
#     return render(request,'home.html',{})


class HomeView(ListView):
    model = Post
    template_name = "home.html"


class ArticleView(DetailView):
    model = Post
    template_name = "articles.html"


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "create.html"
    # fields = "__all__"
    # fields = ("fields name")
