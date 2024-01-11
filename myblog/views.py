from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request,'home.html',{})


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-post_date"]


class ArticleView(DetailView):
    model = Post
    template_name = "articles.html"


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "create.html"
    # fields = "__all__"
    # fields = ("fields name")


class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "update.html"


class DeletePost(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("home")
