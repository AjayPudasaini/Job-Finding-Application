from django.urls import path
from blog import views
from blog.views import BlogListView, BlogDetailView
urlpatterns = [
    path('blog/list', BlogListView.as_view(), name = 'blog-list'),
    path('blog/detail/<str:slug>', BlogDetailView.as_view(), name='blog-detail')
]
