from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.paginator import Paginator
from .models import Post, Category, Featured
from .forms import PostForm, EditForm
from django.urls import reverse_lazy



# class CategoryView(TemplateView):
#     model = Post
#     template_name = 'categories.html'
#     ordering = ['-post_date']

#     def get_context_data(self, cats, *args, **kwargs):
#         cat_menu = Category.objects.all()
#         feat_menu = Featured.objects.all()
#         context = super(CategoryView, self).get_context_data(*args, **kwargs)
#         category_posts = Post.objects.filter(category=cats.replace('-', ' '))
#         context["cat_menu"] = cat_menu
#         context["feat_menu"] = feat_menu
#         context.update({'cats':cats, 'category_posts':category_posts})
#         return context

class CategoryView(ListView):
    model = Post
    template_name = 'categories.html'
    ordering = ['-post_date']
    paginate_by = 2

    def get_queryset(self):
        context = super(CategoryView, self).get_queryset()
        cats = self.kwargs['cats']
        return context.filter(category=cats.replace('-', ' '))

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        feat_menu = Featured.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        cats = self.kwargs['cats']
        context.update({'cat_menu':cat_menu, 'feat_menu':feat_menu, 'cats':cats})
        return context


# class HeroView(TemplateView):
#     model = Post
#     template_name = 'featured_heroes.html'
#     ordering = ['-post_date']

#     def get_context_data(self, hero, *args, **kwargs):
#         cat_menu = Category.objects.all()
#         feat_menu = Featured.objects.all()
#         context = super(HeroView, self).get_context_data(*args, **kwargs)
#         hero_posts = Post.objects.filter(featured=hero.replace('-', ' '))
#         context["cat_menu"] = cat_menu
#         context["feat_menu"] = feat_menu
#         context.update({'hero':hero, 'hero_posts':hero_posts})
#         return context


class HeroView(ListView):
    model = Post
    template_name = 'featured_heroes.html'
    ordering = ['-post_date']
    # paginate_by = 1

    def get_queryset(self):
        context = super(HeroView, self).get_queryset()
        hero = self.kwargs['hero']
        return context.filter(featured=hero.replace('-', ' '))

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        feat_menu = Featured.objects.all()
        context = super(HeroView, self).get_context_data(*args, **kwargs)
        context.update({'cat_menu':cat_menu, 'feat_menu':feat_menu})
        return context


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        feat_menu = Featured.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["feat_menu"] = feat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        feat_menu = Featured.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["heroes"] = context["object"].heroes.all()
        context["cat_menu"] = cat_menu
        context["feat_menu"] = feat_menu
        return context



class AddReviewView(CreateView):
    model = Post
    form_class = PostForm #specifies which fields are shown
    template_name = 'add_review.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        feat_menu = Featured.objects.all()
        context = super(AddReviewView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["feat_menu"] = feat_menu
        return context



class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    ordering = []

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        feat_menu = Featured.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["feat_menu"] = feat_menu
        return context



class AddHeroView(CreateView):
    model = Featured
    template_name = 'add_hero.html'
    fields = '__all__'
    ordering = []

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        feat_menu = Featured.objects.all()
        context = super(AddHeroView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["feat_menu"] = feat_menu
        return context




class UpdateReviewView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_review.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        feat_menu = Featured.objects.all()
        context = super(UpdateReviewView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["feat_menu"] = feat_menu
        return context


    # def get(self, *args, **kwargs):
    #     if self.get_object().author != self.request.user:
    #         raise Http404
    #     return UpdateView.get(self, request, **kwargs)

class DeleteReviewView(DeleteView):
    model = Post
    template_name = 'delete_review.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        feat_menu = Featured.objects.all()
        context = super(DeleteReviewView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["feat_menu"] = feat_menu
        return context

