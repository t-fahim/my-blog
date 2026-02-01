from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blogs.models import Category,Blog
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from .forms import Category_form, Blog_post_form, Add_user_form ,Edit_user_form

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context = {
        'category_count':category_count,
        'blog_count':blog_count,
    }
    return render(request, 'dashboard/dashboard.html',context=context)

@login_required(login_url='login')
def categories(request):

    return render(request,'dashboard/categories.html')

@login_required(login_url='login')
def add_category(request):
    if request.method == "POST":
        form = Category_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = Category_form()
    context = {
        'Category_form':form,
    }
    return render(request, 'dashboard/add_category.html',context=context)

@login_required(login_url='login')
def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        form = Category_form(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = Category_form(instance=category)
    context = {
        'category_form':form,
        'category':category,
    }
    return render(request, 'dashboard/edit_category.html',context=context)

@login_required(login_url='login')
def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

@login_required(login_url='login')
def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts,
    }
    return render(request,'dashboard/post.html',context=context)

@login_required(login_url='login')
def add_post(request):
    if request.method == "POST":
        form = Blog_post_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect('posts')

    form = Blog_post_form()
    context = {
        'blog_post_form':form,
    }
    return render(request,'dashboard/add_post.html',context=context)  

@login_required(login_url='login')
def edit_post(request,pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = Blog_post_form(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect('posts')
    form = Blog_post_form(instance=post)
    context = {
        'blog_post_form':form,
        'post':post
    }
    return render(request, 'dashboard/edit_post.html',context=context)

@login_required(login_url='login')
def delete_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')
  
@login_required(login_url='login')  
def users(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'dashboard/users.html', context=context)  
    

@login_required(login_url='login')
def add_user(request):
    if request.method == "POST":
        form = Add_user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        
    form = Add_user_form()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_user.html',context=context)


@login_required(login_url='login')
def edit_user(request,pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = Edit_user_form(request.POST, instance=user)
        if form.is_valid():       
            user.save()
            return redirect('users')
    form = Edit_user_form(instance=user)
    context = {
        'form':form,
        'user':user
    }
    return render(request, 'dashboard/edit_user.html',context=context)

@login_required(login_url='login')
def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')