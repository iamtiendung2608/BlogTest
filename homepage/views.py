import imp
from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
class ViewPost(DetailView):
    model = Post
    template_name = 'details.html'