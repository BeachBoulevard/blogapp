from django.urls import path

from .views import (HomePageView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView)

urlpatterns = [
    path('post/<int:pk>/delete/',
        PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/',
        PostUpdateView.as_view(), name='post_edit'),
    path('', HomePageView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

]