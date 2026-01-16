from django.contrib import admin
from .models import Categories, Blogs


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','author','status','is_featured')
    search_fields = ('id','title','category__category_name','status','author__username')

admin.site.register(Categories)
admin.site.register(Blogs,BlogAdmin)