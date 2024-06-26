"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),#13
    path('admin/', admin.site.urls),
   # path('', include('app.urls')),
    path('ule/', views.ule, name='ule'),#13
    path('signup', views.signup_page, name='signup_page'),#14
    path('login', views.login_page, name='login_page'),#14
    path('logout', views.logout_page, name='logout_page'),#14
    path('ulnowy/', views.ul_nowy, name='ul_nowy'),
    path('<int:pk>/uldetal/', views.uldetal, name='detalUl'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
]
