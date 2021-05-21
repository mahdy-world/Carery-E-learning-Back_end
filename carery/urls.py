"""carery URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Applications
    path('auth/', include('django.contrib.auth.urls')),
    path('contact_us/', include('Contact_Us.urls', namespace ='contact')),
<<<<<<< HEAD
    path('student/', include('Student.urls', namespace ='students')),
    path('core/', include('Core.urls', namespace ='cors')),
    path('book/', include('Book.urls', namespace ='books')),
    path('team/', include('team.urls', namespace ='team')),
    path('trainer/', include('Trainer.urls', namespace ='trainer')),
=======
    # path('student/', include('Student.urls', namespace ='students')),
    path('Books/', include('Book.urls', namespace ='Books')),
    path('Teams/', include('team.urls', namespace ='Teams')),
    path('Trainers/', include('Trainer.urls', namespace ='Trainers')),
>>>>>>> 17670b6f1b84498da85d5855d435552836a7a3bb

]
