from django.shortcuts import render, redirect
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


class BlogListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog_list.html'
    context_object_name = 'post'
    paginate_by = 20


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

