from django.urls import path
from .views import HomeView, ArticleDetailView, AddReviewView, UpdateReviewView, DeleteReviewView

urlpatterns = [
    
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_review/', AddReviewView.as_view(), name='add_review'),
    path('article/edit/<int:pk>', UpdateReviewView.as_view(), name="update_review"),
    path('article/<int:pk>/delete/', DeleteReviewView.as_view(), name="delete_review"),

]  