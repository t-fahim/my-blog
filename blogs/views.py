from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Category, Comment, AboutMe, SocialProfile
from django.db.models import Q

# Create your views here.
def posts_by_category(request,category_id):
    # 1. Get the single most recent featured post for this category
    # Use .first() to get one object or None
    featured_post = Blog.objects.filter(
        is_featured=True, 
        status='Published', 
        category=category_id
    ).order_by('-updated_at').first()
    
    # fetch the post that belogs to the category with the category_id
    all_posts = Blog.objects.filter(
        status='Published', 
        category=category_id
    ).order_by('-updated_at')

    # 3. If a featured post exists, exclude it from the main list
    if featured_post:
        posts = all_posts.exclude(id=featured_post.id)
    else:
        posts = all_posts
    # try:
    #     category = Categories.objects.get(pk = category_id)
    # except:
    #     return redirect('home')

    category = get_object_or_404(Category,pk = category_id)
    context = {
        'featured_post':featured_post,
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context=context)


def blog(request,slug):
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    # author social link
    social_links = SocialProfile.objects.filter(user = single_blog.author)
    # author about me
    about = getattr(single_blog.author, 'aboutme', None)
    # print(about)
    # print(social_links)
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # comments
    comments = Comment.objects.filter(blog = single_blog)
    comments_count = comments.count()
    # print(comments)
    context = {
        'single_blog':single_blog,
        'comments':comments,
        'comments_count':comments_count,
        'social_links':social_links,
        'about':about,
    }
    return render(request, 'blog.html', context=context)


def search(request):
    keyword = request.GET.get('keyword')
    # print(keyword)
    blogs = Blog.objects.filter(
        Q(title__icontains=keyword) | 
        Q(short_description__icontains=keyword) | 
        Q(blog_body__icontains=keyword), 
        status = 'Published')
    # print(blogs)
    context = {
        'keyword':keyword,
        'blogs':blogs,
    }
    return render(request, 'search.html', context=context)