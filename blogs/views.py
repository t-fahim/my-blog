from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blogs, Categories

# Create your views here.
def posts_by_category(request,category_id):
    # fetch the post that belogs to the category with the category_id
    posts = Blogs.objects.filter(status = 'Published', category = category_id)
    # try:
    #     category = Categories.objects.get(pk = category_id)
    # except:
    #     return redirect('home')

    category = get_object_or_404(Categories,pk = category_id)
    context = {
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context=context)