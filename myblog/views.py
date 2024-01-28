from django.views.generic import ListView
from myblog.models import Category
from django import template
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        which_post = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = which_post.total_likes()
        context["total_likes"] = total_likes
        return context


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "update.html"


class DeletePost(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("home")


class CategoryView(ListView):
    model = Post
    template_name = "category_view.html"
    context_object_name = 'posts'
    ordering = ["-post_date"]

    def get_queryset(self):
        category_id = self.kwargs['pk']
        category = Category.objects.get(pk=category_id)
        queryset = Post.objects.filter(category=category)
        return queryset.order_by(*self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['pk']
        context['category'] = Category.objects.get(pk=category_id)
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
