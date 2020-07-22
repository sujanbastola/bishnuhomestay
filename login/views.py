from django.shortcuts import render, HttpResponse, redirect
from .models import contact, carusel
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout
from blog.models import Post
from gallery.models import imggal



# Create your views here
# blog arange
def login(request):
    allPosts = Post.objects.order_by('-timeStamp')[:2]
    allimggal = imggal.objects.order_by('-timeStamp')[:2]
    context = {
        'allPosts': allPosts,
        'allimggal': allimggal,
    }
    return render(request, 'suru/login1.html', context)






# def login(request):
#     allPosts = Post.objects.order_by('-timeStamp')[:2]
#     context = {'allPosts': allPosts}
#     return render(request, 'suru/login1.html', context)
# for gallery
def arangegal(request):
    allimggal = imggal.objects.order_by('-timeStamp')[:2]
    context = {'allimggal': allimggal}
    return render(request, 'suru/login1.html', context)


# for carusel img
# def carusel(request):
#     caruseldisplay = carusel.objects.all()
#     return render(request, 'suru/login1.html', {'carusel': caruseldisplay})

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug)
    if post.exists():
        post = post.first()
    else:
        return render(request, 'suru/index.html')

    context = {'post': post}
    return render(request, 'suru/blogpost.html', context)


def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        if len(name) < 2 or len(email) < 3 or len(phone) < 4 or len(content) < 5:
            messages.error(request, "please fill the form correctly")
        else:
            done = contact(name=name, phone=phone, email=email, content=content)
            done.save()
            messages.success(request,"your message has been successfully sent")
    return render(request, 'suru/contact.html')

def about(request):
    return render(request, 'suru/about1.html')



def book(request):
    return render(request, 'suru/book.html')

def search(request):
    query = request.GET['query']
    if len(query) > 50:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)

        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request, "No Search found. Please refine your query")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'suru/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        #get the post parameter
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous inputs
        #username should be under 10 characters
        if len(username) > 10:
            messages.error(request, "username must be under 10 characters")
            return redirect('/')
        #username should be alphnumeric
        if not username.isalnum():
            messages.error(request, "username should only contain letters and numbers")
            return redirect('/')
        #passwords should match
        if pass1 != pass2:
            messages.error(request, "passwords do not match")
            return redirect('/')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('/')
    else:
        return render(request, 'suru/index.html')

def handle_Login(request):
    if request.method == 'POST':
        #Get the parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            dj_login(request, user)
            messages.success(request, "Successfully logged In")
            return redirect('/')

        else:
            messages.error(request, "Invalid inputs Please try again")
            return redirect('/')
    return render(request, 'suru/index.html')


def handle_Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def carusel(request):
    resultsdisplay = imggal.objects.all()
    return render(request, 'suru/login1.html', {'imggal': resultsdisplay})








