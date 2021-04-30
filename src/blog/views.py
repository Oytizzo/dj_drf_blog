from django.shortcuts import render

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '2021-05-01'
    },
    {
        'author': 'John Smith',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '2021-05-02'
    }
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'about',
    }
    return render(request, 'blog/about.html', context)
