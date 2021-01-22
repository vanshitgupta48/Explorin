# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# Views
from users import views as users_views
from .views import (index, about, projects, contact, flexbox, bonus, advance, week2bonus, video, project1)
# Para poder visualizar las imgs durante desarrollo se agrega el mas y la linea
# Ademas se deben cambiar la mediaurl y media root en settings
urlpatterns = [
    path("", index, name="index"),
    path('about/', about, name = 'about'),
    path('projects/', projects, name = 'projects'),
    path('contact/', contact, name = 'contact'),
    path('flexbox/', flexbox, name = 'flexbox'),
    path('bonus/', bonus, name = 'bonus'),
    path('advance/', advance, name = 'advance'),
    path('week2bonus/', week2bonus, name = 'week2bonus'),
    path('video/', video, name = 'video'),
     path('project1/', project1, name = 'project1'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)