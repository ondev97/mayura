from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from decouple import config
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from mayuraweb.models import *

# Create your views here.

def index(request):
    sec1 = HomeSection.objects.filter().first()
    sec2 = ProductSection.objects.filter().first()
    sec3 = Product.objects.all()[:3]
    sec4 = MaterialSection.objects.filter().first()
    sec5 = TestimonialSection.objects.filter().first()
    sec6 = VideoBlogSection.objects.filter().first()
    sec7 = BlogPost.objects.filter(display_in_homepage=True)[:3]
    data = {
        'sec1' : sec1,
        'sec2' : sec2,
        'sec3' : sec3,
        'sec4' : sec4,
        'sec5' : sec5,
        'sec6' : sec6,
        'sec7' : sec7
    }
    return render(request, 'index.html', data)

def contact(request):
    c = ContactUs.objects.filter().first()
    data = {
        'sec1': c
    }
    return render(request, 'contact.html', data)

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_no = request.POST['contact']
        email = request.POST['e_mail']
        subject = 'MESSAGE FROM MAYURA WEBSITE'
        message = request.POST['message']
        msg = 'From : '+ email + '\nFull Name : '+ name + '\nContact Number : ' + phone_no + '\nMessage : ' + message + '\n'
        to_email = [config('TO_EMAIL', cast=str)]

        try:
            send_mail(subject,msg,email, to_email, fail_silently=False)
            response = {
                'message': 'Question was sent successfully...'
            }
            return JsonResponse(response, status=200)
        except Exception as e:
            print(e)
            response = {
                'message': 'Question was not sent...'
            }
            return JsonResponse(response, status=400)

def who_are_we(request):
    d = WhoAreWe.objects.filter().first()
    data = {
        'sec1' : d
    }
    return render(request, 'whoAreWe.html', data)

def blog(request):
    blog = BlogPage.objects.filter().first()
    featured_blogs = BlogPost.objects.filter(is_featured=True)
    posts = BlogPost.objects.filter(is_featured=False)
    allposts = BlogPost.objects.all()
    data = {
        'blogpage' : blog,
        'featured_posts' : featured_blogs,
        'other_posts' : posts
    }
    return render(request, 'blog.html', data)

def blog_post(request, id):
    posts = BlogPost.objects.all()
    post = BlogPost.objects.filter(slug=id).first()
    comments = Comment.objects.filter(blogpost=post)
    if not post:
        post = BlogPost.objects.filter().first()

    p = get_position(posts, post)
    if p == 0:
        previous = 0
    else:
        previous = posts[p-1].slug
    if p < len(posts)-1:
        next = posts[p+1].slug
    else:
        next = 0
    data = {
        'post' : post,
        'previous' : previous,
        'next' : next,
        'comments' : comments
    }
    return render(request, 'blogPost.html', data)

def comment(request):
    response = {
        'message': 'You have added a comment successfully...'
    }
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        website = request.POST['website']
        email = request.POST['email']
        comment = request.POST['comment']
        post = BlogPost.objects.get(id=id)
        Comment.objects.create(blogpost=post, comment=comment, name=name, email=email, website=website)
        return JsonResponse(response, status=200)

def get_position(list, value):
    for index, item in enumerate(list):
        if item==value:
            print(item)
            return index
    return 0