from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author

# Create your views here.
def home(request):
    return render(request, 'home.html')

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':all_posts})
    # post_list = ""
    # for post in posts:
    #     post_list += f"<li><h3>{post.title}</h3><p>{post.author.name}</p></li>"
    # response = f"<h1>All posts:</h1><ul>{post_list}</ul>"
    # return HttpResponse(response)

def post(request, id):
    try:
        p = Post.objects.get(id=id)
    except:
        p = False
    return render(request, 'post.html', {'post':p})