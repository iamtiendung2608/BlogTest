from .views import BlogListView, ViewPost

from django.urls import path

urlpatterns = [
    path('post/<int:pk>/',ViewPost.as_view(), name='details' ),
    path('', BlogListView.as_view(),name='home'),

]