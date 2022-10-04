from re import L
# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'



class AddReviewView(CreateView):
    model = Post
    form_class = PostForm #specifies which fields are shown
    template_name = 'add_review.html'



class UpdateReviewView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_review.html'



class DeleteReviewView(DeleteView):
    model = Post
    template_name = 'delete_review.html'
    success_url = reverse_lazy('home')