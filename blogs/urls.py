
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('<int:category_id>',views.posts_by_category, name='posts_by_category'),
]
