from django.contrib import admin
from .models import Category, Blog, Comment, AboutMe, SocialProfile


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','author','status','is_featured',)
    search_fields = ('id','title','category__category_name','status','author__username',)
    list_editable = ('is_featured','status',)

class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ('user','platform','link',)
    search_fields = ('user__username',)

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('user', 'about_heading', 'created_at')
    search_fields = ('user__username',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'comment', 'created_at', 'updated_at')
    search_fields = ('user__username', 'blog__title', 'comment')


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(SocialProfile, SocialProfileAdmin)