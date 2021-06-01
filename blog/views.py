from datetime import date
from django.http import request
from django.shortcuts import render



all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "1.jpeg",
        "author": "Griffin2021",
        "date": date(2021, 6, 1),
        "title": "Mountain Hiking",
        "excerpt": "The technology of the future !!!",
        "content": """  Lorem ipsum dolor sit amet, 
            consectetur adipisicing elit. Libero nemo dolorum veniam eligendi laborum quas beatae, expedita provident asperiores excepturi aut 
            blanditiis animi facilis obcaecati repudiandae porro. Numquam, id fugit. """

    },

    {
        "slug": "coding-is-fun",
        "image": "2.jpeg",
        "author": "Griffin2022",
        "date": date(2019, 2, 22),
        "title": "Hardcoding bla ",
        "excerpt": "Code your Ideas",
        "content": """  Lorem ipsum dolor sit amet, 
            consectetur adipisicing elit. Libero nemo dolorum veniam eligendi laborum quas beatae, expedita provident asperiores excepturi aut 
            blanditiis animi facilis obcaecati repudiandae porro. Numquam, id fugit. """

    },
      {
        "slug": "coding-is-maybe-fun",
        "image": "1.jpeg",
        "author": "Griffin2022",
        "date": date(2019, 2, 22),
        "title": "Hardcoding bla bla ",
        "excerpt": "Code your Ideasddd",
        "content": """  Lorem ipsum dolor sit amet, 
            consectetur adipisicing edfdfdsfdsfgflit. Libero nemo dolorum veniam eligendi laborum quas beatae, expedita provident asperiores excepturi aut 
            blanditiis animi facilis obcaecati repudiandae porro. Numquam, id fugit. """

    }
]


def get_date(post):
    return post['date']


# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })  # connected with path --> starting-page


def posts(request):
    return render(request, 'blog/all-posts.html')  # connected with path --> posts-page


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")  # connected with path --> post-detail-page
