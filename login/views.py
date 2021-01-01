from django.shortcuts import render, HttpResponse, redirect
from .models import contact, carusel
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout
from blog.models import Post
from gallery.models import imggal
from Rooms.models import room, Reservation
from django.core.mail import send_mail
from django.conf import settings
import datetime



# Create your views here
# blog arange
def login(request):
    allPosts = Post.objects.order_by('-timeStamp')[:2]
    allimggal = imggal.objects.order_by('-timeStamp')[:3]
    allroom = room.objects.order_by('-timeStamp')[:3]
    caruseldisplay = carusel.objects.all()
    context = {
        'allPosts': allPosts,
        'allimggal': allimggal,
        'carusel': caruseldisplay,
        'allroom' : allroom,

    }
    return render(request, 'suru/login1.html', context)




def about(request):
    return render(request, 'suru/about1.html')


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
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("contact")

        subject = message
        from_email = settings.DEFAULT_FROM_EMAIL
        to_EMAIL = [email]

        send_mail(
            subject,message, from_email, to_EMAIL, fail_silently=True
        )

    return render(request, 'suru/contact.html')




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


# For booking the room
def book_room(request):
    if request.method == "POST":

        room_id = request.POST['room_id']

        room = rooms.objects.all().get(id=room_id)
        # for finding the reserved rooms on this time period for excluding from the query set
        for each_reservation in Reservation.objects.all().filter(room=room):
            if str(each_reservation.check_in) < str(request.POST['check_in']) and str(each_reservation.check_out) < str(
                    request.POST['check_out']):
                pass
            elif str(each_reservation.check_in) > str(request.POST['check_in']) and str(
                    each_reservation.check_out) > str(request.POST['check_out']):
                pass
            else:
                messages.warning(request, "Sorry This Room is unavailable for Booking")
                return redirect("homepage")

        current_user = request.user
        total_person = int(request.POST['person'])
        booking_id = str(room_id) + str(datetime.datetime.now())

        reservation = Reservation()
        room_object = room.objects.all().get(id=room_id)
        room_object.status = '2'

        user_object = User.objects.all().get(username=current_user)

        reservation.guest = user_object
        reservation.room = room_object
        person = total_person
        reservation.check_in = request.POST['check_in']
        reservation.check_out = request.POST['check_out']

        reservation.save()

        messages.success(request, "Congratulations! Booking Successfull")

        return redirect("homepage")
    else:
        return HttpResponse('Access Denied')








