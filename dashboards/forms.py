from django import forms
from blogs.models import Category


class Category_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'