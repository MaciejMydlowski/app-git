from django.views import View#18
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect    #Funkcja redirect jest odpowiedzialna za przekierowania na inne strony.
from django.http import HttpResponse #1
from django.template import loader#5
#contrib jest to paczka zawierająca różne frameworki.
from django.contrib.auth.models import User#15  Klasa User jest odpowiedziala za wiele czynności związanych z użytkownikami.
from django.contrib.auth import authenticate#15 Metoda authenticate jest odpowiedzialna za weryfikowanie użytkownika.
from django.contrib import auth #15 auth jest to framework słóżący do autoryzacji.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required#18
from django.contrib.auth.mixins import LoginRequiredMixin#18
from .forms import PosiadaneUleForm
from .models import PosiadaneUle

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

#@login_required
def ule(request):
    ul = PosiadaneUle.objects.order_by('nazwa')
    context = {
        'ul': ul,
    }
    return render(request, 'app/ule.html', context)

def uldetal(request, pk):
    uld = PosiadaneUle.objects.get(pk=pk)
    context = {
        'uld': uld,
    }
    return render(request, 'app/uldetal.html', context)

def ul_nowy(request):
    #post = PosiadaneUleForm()
    if request.method == "POST":
        form = PosiadaneUleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)   
            #PosiadaneUle.objects.create(**form.cleaned_data)
            post = form.save(commit=False)
            post.install_date = timezone.now()
            post.matka_date = timezone.now()
            post.save()
            form.save_m2m()
            print(post.pk)
            return redirect( 'detalUl', pk=post.pk)
        else:
            print(form.errors)

    else:
        form = PosiadaneUleForm()
    return render(request, 'app/ul_nowy.html', {'form': form})
 



 
    





