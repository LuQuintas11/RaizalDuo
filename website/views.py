from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Show, Video, VideoMusic, Comment
from .forms import CommentForm
from . import models
from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class PostList(generic.ListView):
    def get(self, request, slug=None, *args, **kwargs):
        posts = Post.objects.filter(status=1).order_by("-created_on")
        videos = Video.objects.all()
        return render(
            request,
            "index.html",
            {
                "posts": posts,
                "shows": Show.objects.all(),
                "videos": videos,
            },
        )


def PostDetail(request, post_id, *args, **kwargs):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, id=post_id)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    liked = request.user in post.likes.all()

    return render(
        request,
        "post_details.html",
        {
            "post": post,
            "comments": comments,
            "liked": liked,
            "video": post.video.filter(),
        },
    )


def createComment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "GET":
        return render(
            request, "createComment.html", {"form": CommentForm(), "post": post}
        )
    else:
        try:
            form = CommentForm(request.POST)
            newComment = form.save(commit=False)
            newComment.user = request.user
            newComment.post = post
            newComment.save()
            messages.success(request, "Your comment is awaiting approval")
            return redirect(reverse("PostDetail", args=[newComment.post.id]))

        except ValueError:
            return render(
                request,
                "createComment.html",
                {"form": CommentForm(), "error": "bad data passed in"},
            )


@login_required
def updateComment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == "GET":
        form = CommentForm(instance=comment)
        return render(
            request, "updateComment.html", {"comment": comment, "form": form}  # noqa
        )
    else:
        try:
            form = CommentForm(request.POST, instance=comment)
            form.save()
            messages.success(request, "Successfully updated review!")
            return redirect(reverse("PostDetail", args=[comment.post.id]))
        except ValueError:
            return render(
                request,
                "updateComment.html",
                {"comment": comment, "form": form, "error": "Bad data in form"},
            )


@login_required
def deleteComment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    comment.delete()
    messages.success(request, "Your comment has been deleted")
    return redirect(reverse("PostDetail", args=[comment.post.id]))


def PostLike(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    post.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
