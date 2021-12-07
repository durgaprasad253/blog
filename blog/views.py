from django.shortcuts import render
from datetime import date
all_posts=[
    {
        'slug':"hike-in-the-mountains",
        'img':'mountain.jpg',
        'author':'Durga Prasad',
        'date':date(2021,12,7),
        'title':'Mountain Hiking',
        'excert':'I love Hiking and its all about enjoying the nature and I hope you guys will love it too',
        'content':"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque laudantium obcaecati qui quae recusandae facilis quam iure
         neque ex saepe vero inventore, libero velit eligendi minus possimus tempore necessitatibus laboriosam.
        """
    },
    {
        
        'slug':"programming-is-fun",
        'img':'laptop.jpg',
        'author':'DP',
        'date':date(2022,11,7),
        'title':'Programming-is great',
        'excert':'I love programming and its really fun to code and learn',
        'content':"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque laudantium obcaecati qui quae recusandae facilis quam iure
         neque ex saepe vero inventore, libero velit eligendi minus possimus tempore necessitatibus laboriosam.

         Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque laudantium obcaecati qui quae recusandae facilis quam iure
         neque ex saepe vero inventore, libero velit eligendi minus possimus tempore necessitatibus laboriosam.
        """
    
    },
    {
        
        'slug':"Nature-is-fun",
        'img':'nature.jpg',
        'author':'Durga Prasad D',
        'date':date(2022,5,4),
        'title':'Nature-is-great',
        'excert':'I love Nature and its really fun',
        'content':"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque laudantium obcaecati qui quae recusandae facilis quam iure
         neque ex saepe vero inventore, libero velit eligendi minus possimus tempore necessitatibus laboriosam.

         Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque laudantium obcaecati qui quae recusandae facilis quam iure
         neque ex saepe vero inventore, libero velit eligendi minus possimus tempore necessitatibus laboriosam.

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque laudantium obcaecati qui quae recusandae facilis quam iure
         neque ex saepe vero inventore, libero velit eligendi minus possimus tempore necessitatibus laboriosam.

        """
    
    }
    
]

def get_date(posts):
    return posts['date']
# Create your views here.
def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts(request):

    return render(request,"blog/all-posts.html",{
        'all_posts':all_posts
    })

def post_details(request,slug):
    identified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request,"blog/post-details.html",{
        "post":identified_post
    })