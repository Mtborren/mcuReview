from django import forms
from datetime import date
from .models import Post, Featured, Category



choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


featured_choices = Featured.objects.all().values_list('name', 'name')
featured_list = []
for item in featured_choices:
    featured_list.append(item)




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "header_image", "category", "featured", "year", "director", "body", "rating"]


        widgets = {

            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'featured': forms.CheckboxSelectMultiple(choices=featured_choices, attrs={'class': ''}),
            # 'heroes': forms.ModelMultipleChoiceField(queryset=Featured.objects.all(), to_field_name="name"),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.Select(choices=[tuple([x,x]) for x in range(date.today().year, 2000, -1)], attrs={'class': 'form-control'}),
            'rating': forms.Select(choices=[tuple([x,x]) for x in range(10, 0, -1)], attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "header_image", "category", "featured", "year", "director", "body", "rating"]


        widgets = {

            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'featured': forms.CheckboxSelectMultiple(choices=featured_choices, attrs={'type':'checkbox', 'class': ''}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.Select(choices=[tuple([x,x]) for x in range(date.today().year, 2000, -1)], attrs={'class': 'form-control'}),
            'rating': forms.Select(choices=[tuple([x,x]) for x in range(10, 0, -1)], attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),

        }