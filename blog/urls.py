from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogView, CreatePostView, BlogListView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list/', BlogView.as_view(), name='blog_list'),
    path('create_post_view/', CreatePostView.as_view(), name='create_post'),
    path('page/', BlogListView.as_view(), name='page'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
