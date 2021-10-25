from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.


################################################################

# def home(request):
#    return HttpResponse('hello de nuevo')


################################################################

def edit(request, post_id):
    if request.method == 'GET':
        posts = Post.objects.get(id=post_id)
        context = {
            'posts': posts}
        return render(request, 'edit.html', context)

    else:
        posts = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())


################################################################


def base(request):

    return render(request, 'base.html')


################################################################
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all()[:20]
    context = {
        'posts': posts}
    return render(request, 'index.html', context=context)


################################################################
def delete(request, post_id):

    posts = Post.objects.get(id=post_id)
    posts.delete()
    return HttpResponseRedirect(str('/'))
##################################################################

def like(request, post_id):

    post = Post.objects.get(id=post_id)
    cont = post.like_count + 1 
    post.like_count = cont 
    post.save()
    return HttpResponseRedirect('/')
