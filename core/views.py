from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPostForm, CommentForm
from .models import Post, Comment
from django.db.models import Q



def create_blogPost_view(request):
    form = BlogPostForm()
    if request.method == "POST":
        form = BlogPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect("home")
    context = dict(form=form)
    return render(request, "pages/create_post.html", context)


def update_blogPost_view(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect("post_detail", pk=post.id)
    else:
        form = BlogPostForm(instance=post)
    context = dict(form=form)
    return render(request, "pages/create_post.html", context)


def single_post_view(request):
    all_post = Post.objects.filter(is_published=True)
    context = dict(all_post=all_post)
    return render(request, "pages/blog.html", context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(data=request.POST)
    comments = post.comments.filter(parent__isnull=True)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return redirect("post_detail", id=post.id)
    else:
        form = CommentForm()
    post.view_count += 1
    post.save()
    context = dict(post=post, form=form, comments=comments)
    return render(request, "pages/blog-details.html", context)


# Create your views here.
def about_view(request):
    context = dict()
    return render(request, "pages/about.html", context)


def search(request):
    search_posts = None
    post_count = 0
    if request.method == "GET":
        keyword = request.GET["keyword"]
        if keyword:
            search_posts = (
                Post.objects.order_by("-date_posted")
                .filter(Q(content__icontains=keyword) | Q(title__icontains=keyword))
                .distinct()
            )
            post_count = search_posts.count()

    context = {
        "search_posts": search_posts,
        "post_count": post_count,
    }
    return render(request, "pages/search_result.html", context)
