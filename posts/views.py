from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name= 'all_posts_list'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'description']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    