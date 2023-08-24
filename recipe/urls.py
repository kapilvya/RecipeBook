
from django.urls import path
from . import views
from .views import (PostListView ,
                    PostDetailView ,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
                    )

urlpatterns = [
    path('',PostListView.as_view(), name='recipe-home' ),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail' ),
    path('post/new/',PostCreateView.as_view(), name='post-create' ),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update' ),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete' ),
    # <int:pk> primary key
    
    path('about/',views.about, name='recipe-about' ),
]


#looking for <app>/<model>_<viewtype>.html
