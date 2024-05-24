from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
#from .models import Post
from .models import Przeglad

# Create your views here.
#def post_list(request):
   # return render(request, 'blog/post_list.html', {})
def wpisy_przegladow(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #przeglad_views = Przeglad.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    przeglad_views = Przeglad.objects.all()
    return render(request, 'app/wpisy_przegladow.html', {'przeglad_views': przeglad_views})

def post_detail(request, pk):
    Przeglad.objects.get(pk=pk)
    post = get_object_or_404(Przeglad, pk=pk)
    #post = Przeglad.objects.all()
    return render(request, 'app/post_detail.html', {'post': post})

