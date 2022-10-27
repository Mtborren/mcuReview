from django.urls import path
from .views import HomeView, ArticleDetailView, AddReviewView, UpdateReviewView, DeleteReviewView, AddCategoryView, CategoryView, HeroView

urlpatterns = [
    
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_review/', AddReviewView.as_view(), name='add_review'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdateReviewView.as_view(), name="update_review"),
    path('article/<int:pk>/delete/', DeleteReviewView.as_view(), name="delete_review"),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
    path('featured/<str:hero>/', HeroView.as_view(), name='featured'),
    
]