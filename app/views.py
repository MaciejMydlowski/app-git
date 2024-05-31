from django.views import View#18
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect    #Funkcja redirect jest odpowiedzialna za przekierowania na inne strony.
from django.http import HttpResponse #1
from .models import Przeglad
from .forms import PostForm, UlForm
from django.template import loader#5
from .models import DodawanieUla#WatchedMovies, #5
#contrib jest to paczka zawierająca różne frameworki.
from django.contrib.auth.models import User#15  Klasa User jest odpowiedziala za wiele czynności związanych z użytkownikami.
from django.contrib.auth import authenticate#15 Metoda authenticate jest odpowiedzialna za weryfikowanie użytkownika.
from django.contrib import auth #15 auth jest to framework słóżący do autoryzacji.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required#18
from django.contrib.auth.mixins import LoginRequiredMixin#18



# Create your views here.

def home(request):  #15 strona domowa
    return render(request, 'app/home.html')

def signup_page(request):   #15
    context = {}
    if request.method == 'POST':
        # Request for sign up
        # Check if user is available
        try:
            user = User.objects.get(username=request.POST['username'])
            context['error'] = 'Podana nazwa użytkownika już istnieje! Proszę podać inną nazwę użytkownika.'
            return render(request, 'app/signup.html', context)
        except User.DoesNotExist:
            # Check if the password1 is equal to the password2
            if request.POST['password1'] != request.POST['password2']:
                context['error'] = 'Podane hasła nie są takie same! Proszę wprowadzić identyczne hasła.'
                return render(request, 'app/signup.html', context)
            else:
                # Create new user
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # Automatic login after signing up
                auth.login(request, user)
                # Go to home page
                return redirect('home')
    else:
        return render(request, 'app/signup.html', context)
def login_page(request):
    context = {}
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'] ,password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if request.POST.get('redir'):
                return redirect(f"{request.POST.get('redir')}")
            else:
                return redirect('home')
        else:
            context['error'] = 'Podane hasło lub login są błędne! Podaj poprawne dane.'
            if request.POST.get('redir'):
                context['next'] = 'Tylko zalogowani użytkonicy mają dostęp do tej strony! Zaloguj się.'
                context['nextURL'] = request.GET.get('next')
            return render(request, 'app/login.html', context)
    else:
        if request.GET.get('next'):
            context['next'] = 'Tylko zalogowani użytkonicy mają dostęp do tej strony! Zaloguj się.'
            context['nextURL'] = request.GET.get('next')
        return render(request, 'app/login.html', context)
def logout_page(request):#17
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def ule(request):
    movies = WatchedMovies.objects.order_by('title')
    context = {
        'movies': movies,
    }
    return render(request, 'app/ule.html',context)
def ule2(request):
    ul = DodawanieUla.objects.order_by('nazwa')
    context = {
        'ul': ul,
    }
    return render(request, 'app/ule2.html',context)
def uldetal(request, pk):
    DodawanieUla.objects.get(pk=pk)
    ul = get_object_or_404(DodawanieUla, pk=pk)
#    context = {
#        'ul': ul,
#    }
    return render(request, 'app/uldetal.html', {'ul': ul})

def detail(request, watchedMovies_id):
    movie = WatchedMovies.objects.get(pk=watchedMovies_id)
    context = {
        'movie': movie,
    }
    return render(request, 'app/detail.html', context)

def ul_nowy(request):
    if request.method == "POST":
        form = UlForm(request.POST)
        if form.is_valid():
            ul = form.save(commit=False)
            #ul.author = request.user
            #ul.install_date = timezone.now()
            ul.matka_date = timezone.now()
            ul.save()
            #return redirect('detalUl', pk=ul.pk)
        return render(request, 'app/home.html')
    else:
        form = UlForm()
    return render(request, 'app/ul_edit.html', {'form': form})

#9 pk=post.pk
def wpisy_przegladow(request):
    przeglad_views = Przeglad.objects.all()
    return render(request, 'app/wpisy_przegladow.html', {'przeglad_views': przeglad_views})

def post_detail(request, pk):
    Przeglad.objects.get(pk=pk)
    post = get_object_or_404(Przeglad, pk=pk)
    return render(request, 'app/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            typ_ula = form.cleaned_data['typ_ula']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Przeglad, pk=pk)
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
    return render(request, 'app/post_edit.html', {'form': form})

