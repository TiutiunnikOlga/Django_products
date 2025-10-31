from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogView, CreatePostView, BlogListView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list/', BlogView.as_view(), name='blog_list'),
    path('create_post_view/', CreatePostView.as_view(), name='create_post'),
    path('page/', BlogListView.as_view(), name='page'),
    path('blog/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blog_detail'),
]
