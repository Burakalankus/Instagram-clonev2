from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm,CommentForm
from django.contrib import messages, auth
from post.models import Post, Profile ,Follower,Like , Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from random import sample


def index(request):
    if request.user.is_anonymous:
        messages.warning(request, f"Lütfen giriş yapınız.")
        return redirect('post:login')
    
    all_posts = Post.objects.all()
    posts_with_images = [post for post in all_posts if post.image]
    
    comment_form = CommentForm()
    comments = Comment.objects.filter(post__in=all_posts)
    
    # Get a list of random users (excluding the current user)
    random_users = User.objects.exclude(username=request.user.username).order_by('?')[:5]
    
    context = {
        'posts': posts_with_images,
        'comment_form': comment_form,
        'comments': comments,
        'random_users': random_users
    }
    return render(request, "pages/home.html", context)



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user if request.user.is_authenticated else None
            post.save()
            messages.success(request, "Post başarıyla oluşturuldu.")
            return redirect('post:home')
    else:
        form = PostForm()
    return render(request, 'components/create_post.html', {'form': form})

@login_required
def tags(request, tag_slug):
    tag = get_object_or_404(tags, slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-posted')
    return render(request, 'tag.html', {'tag': tag, 'posts': posts})

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        name_surname = request.POST['name_surname']
        username = request.POST['username']
        password = request.POST['password']
        if not len(password) < 3:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email daha önce kullanılmış! Lütfen kullanılmayan email adresi giriniz..')
                return redirect('post:register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Kullanıcı adı daha önce kullanılmış! Lütfen başka kullanıcı adı giriniz..')
                return redirect('post:register')
            else:
                user = User.objects.create_user(email = email, username = username, password = password)
                user.save()
                user_model = User.objects.get(username = username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('post:index')
        else:
            messages.info(request, 'Şifre 3 karakterden fazla olmalıdır.')
            return redirect('post:register')
    else:
        return render(request, 'pages/register.html')
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'E-posta veya şifreniz hatalı, lütfen tekrar deneyiniz..')
            return redirect('post:login')

    return render(request, 'pages/index.html')

@login_required(login_url='login')
def logout_view(request):
    auth.logout(request)
    messages.info(request, 'Çıkış yaptınız..')
    return redirect('post:login')

def like_view(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    existing_like = Like.objects.filter(user=request.user, post=post).first()
    
    if existing_like:
        existing_like.delete()
        post.likes -= 1
        post.save()
        
    else:
        like = Like(user=request.user, post=post)
        like.save()
        post.likes += 1
        post.save()
    
    return redirect('post:home')


def follow_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_to_follow = get_object_or_404(User, id=user_id)

        is_following = Follower.objects.filter(follower=request.user, following=user_to_follow).exists()

        if is_following:
            Follower.objects.filter(follower=request.user, following=user_to_follow).delete()
            messages.success(request, f'Artık {user_to_follow.username} kullanıcısını takip etmiyorsunuz.')
        else:
            Follower.objects.create(follower=request.user, following=user_to_follow)
            messages.success(request, f'{user_to_follow.username} kullanıcısını takip ediyorsunuz.')
    return redirect('post:social')

User = get_user_model()

@login_required

def comment_view(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            profile, created = Profile.objects.get_or_create(user=request.user)
            comment.author = profile  
            comment.post = post
            comment.save()

    return redirect('post:home')

def explore_view(request):
    top_posts = Post.objects.order_by('-likes')[:10]
    # Get a list of random users (excluding the current user)
    random_users = User.objects.exclude(username=request.user.username).order_by('?')[:5]
    
    context = {
        'top_posts': top_posts,
        'random_users': random_users
    }
    return render(request, 'pages/explore.html', context)
