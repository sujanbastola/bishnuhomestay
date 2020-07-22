from django.shortcuts import render, HttpResponse
from .models import Post


# Create your views here.



def blog(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'suru/blog.html', context)


def blogpost(request, slug):
    post = Post.objects.filter(slug=slug)
    if post.exists():
        post = post.first()
    else:
        return render(request, 'suru/index.html')

    context = {'post': post}
    return render(request, 'suru/blogpost.html', context)
