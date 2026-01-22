from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Categories, Blogs


def home(request):
    categories = Categories.objects.all()
    featured_posts = Blogs.objects.filter(is_featured = True, status='Published').order_by('updated_at')
    posts = Blogs.objects.filter(is_featured=False, status='Published')
    context = {
        'categories' : categories,
        'featured_posts' : featured_posts,
        'posts' : posts,
    }
    return render(request,'home.html',context=context)