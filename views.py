from django.shortcuts import render

# blog/views.py
from django.views.generic import ListView, DetailView # Новый

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
# Create your views here.

class BlogDetailView(DetailView): #новое
    model = Post
    template_name = 'post_detail.html'
