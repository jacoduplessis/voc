"""voc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/', views.ApplicationView.as_view(lang='en'), name='apply_en'),
    path('application_success/', views.ApplicationSuccessView.as_view(lang='en'), name='application_success_en'),
    path('aansluiting/', views.ApplicationView.as_view(lang='af'), name='apply_af'),
    path('aansluiting_sukses/', views.ApplicationSuccessView.as_view(lang='af'), name='application_success_af'),
    path('contact/', views.ContactView.as_view(lang='en'), name='contact_en'),
    path('kontak/', views.ContactView.as_view(lang='af'), name='contact_af'),
    path('logo/', views.LogoView.as_view(), name='logo'),
    path('copyright/', views.CopyrightPrivacyView.as_view(), name='copyright_privacy'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('archives/', views.ArchiveView.as_view(), name='archives'),
    path('committee/', views.CommitteeView.as_view(), name='committee'),
    path('links/', views.LinksView.as_view(), name='links'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('navorsing/', views.ResearchListView.as_view(), name='research_list'),
    path('en/', views.IndexView.as_view(lang='en'), name='index_en'),
    path('nl/', views.IndexView.as_view(lang='nl'), name='index_nl'),
    path('', views.IndexView.as_view(lang='af'), name='index_af'),
]
