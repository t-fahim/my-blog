from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Categories, Blogs
from about.models import About


def home(request):
    # categories = Categories.objects.all()
    featured_posts = Blogs.objects.filter(is_featured = True, status='Published').order_by('-updated_at')
    posts = Blogs.objects.filter(is_featured=False, status='Published').order_by('-updated_at')
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        # 'categories' : categories,
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
    }
    return render(request,'home.html',context=context)




