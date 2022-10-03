from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

import cloudinary


def index(request):
    #  If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No,Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.order_by('created_at').reverse().all()[:20]

    # Show
    return render(request, 'posts.html',
                  {'posts': posts})

# / / / Delete


def delete(request, id):
    # Find post
    post = Post.objects.get(id=id)
    post.delete()
   # output = 'POST ID is ' + str(post_id)
    return HttpResponseRedirect('/')

  # /// Edit


def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    print(posts)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    else:
        # Show editting screen
        form = PostForm
        return render(request, 'edit.html',
                      {'posts': posts, 'form': form})

# / / / Likes


def like(request, post_id):
    posts = Post.objects.get(id=post_id)
    new_like = posts.like_count + 1
    posts.like_count = new_like
    print(posts.like_count)
    posts.save()

    return HttpResponseRedirect('/')


def LikeMinus(request, id):
    # Get requested tweet
    posts = Post.objects.get(id=id)
  # Subtract like
    new_like_count = posts.like_count - 1
    posts.like_count = new_like_count
  # Save
    posts.save()
    return JsonResponse({'result': 'successful'})

# Picture


def loadPicture(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = PostForm()
    ctx = {'form': form}
    return render(request, 'posts/post.html', ctx)
