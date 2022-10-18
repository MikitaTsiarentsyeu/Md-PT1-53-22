from datetime import datetime
import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Author
from .forms import AddPost, AddModelPost
from django.contrib.auth.decorators import permission_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

def posts(request):
    'viewed_posts'
    all_posts = Post.objects.all().order_by("-issued")
    viewed_posts = request.session.get('viewed_posts', [])
    return render(request, 'posts.html', {'posts':all_posts, 'viewed_posts': viewed_posts})
    # post_list = ""
    # for post in posts:
    #     post_list += f"<li><h3>{post.title}</h3><p>{post.author.name}</p></li>"
    # response = f"<h1>All posts:</h1><ul>{post_list}</ul>"
    # return HttpResponse(response)

def post(request, id):
    try:
        p = Post.objects.get(id=id)
        viewed_posts = request.session.get('viewed_posts', [])
        if id not in viewed_posts:
            viewed_posts.append(id)
        request.session['viewed_posts'] = viewed_posts
    except:
        p = False
    return render(request, 'post.html', {'post':p})

@permission_required('app.add_post')
def add_post(request):

    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            post = Post()
            post.author = Author.objects.get(email=request.user.email)
            post.issued = datetime.now()
            post.title = form.cleaned_data["title"]
            post.subtitle = form.cleaned_data["subtitle"]
            post.content = form.cleaned_data["content"]
            post.image = form.cleaned_data["image"]
            post.post_type = form.cleaned_data["post_type"]

            post.save()

            return redirect('posts')

    else:
        form = AddPost(initial={'title':'default title value'})

    return render(request, 'add_post.html', {'form':form})

def add_model_post(request):
    if request.method == "POST":
        form = AddModelPost(request.POST, request.FILES)

        post = form.save(commit=False)
        post.author = Author.objects.all()[0]
        post.issued = datetime.now()
        post.save()
        form.save_m2m()
    
        return redirect('posts')

    else:
        form = AddModelPost()

    return render(request, 'add_post.html', {'form':form})
