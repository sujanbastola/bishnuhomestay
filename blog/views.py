from django.shortcuts import render, HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.



def blog(request):
    allPosts = Post.objects.all()
    paginator = Paginator(allPosts,4)
    page =request.GET.get('page')
    try:
        allPosts = paginator.page(page)
    except PageNotAnInteger:
        allPosts = paginator.page(1)
    except EmptyPage:
        allPosts = paginator.page(paginator.num_pages)

    context = {'allPosts': allPosts,
               'page': page,

               }

    return render(request, 'suru/blog.html', context)


def blogpost(request, slug):
    post = Post.objects.filter(slug=slug)
    if post.exists():
        post = post.first()
    else:
        return render(request, 'suru/index.html')

    context = {'post': post}
    return render(request, 'suru/blogpost.html', context)
