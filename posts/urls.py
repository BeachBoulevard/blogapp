from django.urls import path

from .views import HomePageView, PostCreateView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

]