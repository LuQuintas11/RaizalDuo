from . import views
from django.urls import path, include
from django.conf import settings


urlpatterns = [
   
    path('', views.PostList.as_view(), name='home'),
    path('<int:post_id>', views.PostDetail, name='PostDetail'),
    path('like/<int:id>/', views.PostLike, name='post_like'),  
    path("<int:post_id>/create", views.createComment, name="createComment"),
    path("comment/<int:comment_id>", views.updateComment, name="updateComment"),
]

