from django.shortcuts import render

# Create your views here.
def wpisy_przeglądów(request):
    return render(request, 'app/wpisy_przeglądów.html', {})
