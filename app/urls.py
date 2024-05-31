from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [

 #   path('<int:watchedMovies_id>/detail/', views.detail, name='myDetail'),
    path('uldetal/<int:pk>/', views.uldetal, name='detalUl'),


    #path('', views.wpisy_przegladow, name='wpisy_przegladow'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/new', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]

