from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

# posts=[
#     {
#     'author':'Parikshit Hiwase',
#     'title':'Blog Post 1',
#     'content':'Test blog post',
#     'date_posted':'July 31 2023',
#     },
#     {
#     'author':'Test User',
#     'title':'Test Blog Post',
#     'content':'Test blog post 2',
#     'date_posted':'July 31 2023',
#     }

# ]


def home(request):
    # return HttpResponse("<h1>Blog Home</h1>")
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse("<h1>Blog About</h1>")
    return render(request, 'blog/about.html', {'title': "About Page"})
