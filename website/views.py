from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Show, Video
from . import models

class PostList(generic.ListView):
    def get(self, request, slug=None, *args, **kwargs):
        posts = Post.objects.filter(status=1).order_by("-created_on")
        return render (request,  "index.html", 
            {   
            "posts":posts,
            "shows":Show.objects.all(),
            "videos":Video.objects.all()
            
            })


                

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_details.html",
            {   
               
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )









