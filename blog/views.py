from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return  render(request, 'blog/post_edit.html',{'form': form})

def gum(request):
    return render(request, 'blog/content/getusermedia/gum/index.html', {})

def canvas(request):
    return render(request, 'blog/content/getusermedia/canvas/index.html', {})

def resolution(request):
    return render(request, 'blog/content/getusermedia/resolution/index.html', {})

def pc1(request):
    return render(request, 'blog/content/peerconnection/pc1/index.html', {})

def main(request):
    return render(request, 'blog/main.html',{})
def group(request):
    return render(request, 'blog/group.html',{})

def drive(request):
    return render(request, 'blog/drive.html',{})
