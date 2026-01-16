from django.contrib import admin
from .models import Categories, Blogs


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Categories)
admin.site.register(Blogs,BlogAdmin)