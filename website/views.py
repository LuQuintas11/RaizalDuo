from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Show, Video, VideoMusic
from .forms import CommentForm
from . import models
from django import forms
from django.views.generic.edit import FormView




class PostList(generic.ListView):
    def get(self, request, slug=None, *args, **kwargs):
        posts = Post.objects.filter(status=1).order_by("-created_on")
        videos = Video.objects.all()
        return render (request,  "index.html", 
            {   
            "posts":posts,
            "shows":Show.objects.all(),
            "videos":videos,
            
            
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
                "commented": False,
                "liked": liked,
                "video": post.video.filter(),
                "comment_form": CommentForm()

            },
        )

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comments = post.comments.filter(approved=True).order_by("-created_on")
        
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_details.html",
            {   
               
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "video": post.video.filter(),
                

            },
        )



def YouTube(request):
    return render(request, "YouTubeApi.html")






