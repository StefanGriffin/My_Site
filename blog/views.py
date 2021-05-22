from datetime import date
from django.http import request
from django.shortcuts import render

# Create your views here.

post = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpeg",
        "author": "Griffin2021",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "Add a lot of text in here if you feel like it"

    }
]


def starting_page(request):
    return render(request, 'blog/index.html')


def posts(requests):
   pass


def post_detail(requests):
    pass
