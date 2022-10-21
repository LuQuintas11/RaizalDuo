from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Show, Video, VideoMusic
from .forms import CommentForm
from . import models
from django import forms
from django.views.generic.edit import FormView
import requests
from django.conf import settings

import logging

LOGGER = logging.getLogger(__name__)


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

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comments = post.comments.filter(approved=True).order_by("-created_on")
        
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

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

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# def YouTube(request):

#     list_url= 'https://youtube.googleapis.com/youtube/v3/playlists'

#     params={
#         'part' : 'snippet',
#         'q': 'our friends',
#         'channelId': 'UCmAnQ_N8P76uVbrRhrT-1OQ',
#         'key':settings.YOUTUBE_DATA_API_KEY,
#         'maxResults': 3,
#         'type': 'playlists'

#     }
#     r= requests.get(list_url, params=params)
#     results = r.json()['items']

#     for result in results:
#         print(result['id'])
#     return render(request, "YouTubeApi.html")






