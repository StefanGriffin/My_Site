from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Post


# def get_date(post):
#     return post['date']


# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]  # this is a sql command 
    # -date --> desenting order meaning that the last post is gooing to be the first
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })  # connected with path --> starting-page


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts
    })  # connected with path --> posts-page


def post_detail(request, slug):
    # identified_post = next(post for post in all_posts if post['slug']==slug)  
    #post['slug'] is the same thing with {{ post.title }} in the post-detail.html template
    # identified_post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })  # connected with path --> post-detail-page



