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
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/', views.ApplicationView.as_view(), name='application'),
    path('application_success/', views.ApplicationSuccessView.as_view(), name='application_success'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('membership/', views.MembershipView.as_view(), name='membership'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('logo/', views.LogoView.as_view(), name='logo'),
    path('copyright/', views.CopyrightPrivacyView.as_view(), name='copyright_privacy'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('archives/', views.ArchiveView.as_view(), name='archives'),
    path('committee/', views.CommitteeView.as_view(), name='committee'),
    path('links/', views.LinksView.as_view(), name='links'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/<slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('research/', views.ResearchListView.as_view(), name='research_list'),
    path('speakers/', views.SpeakerListView.as_view(), name='speaker_list'),
    path('tours/', views.TourListView.as_view(), name='tour_list'),
    path('medals/', views.MedalListView.as_view(), name='medal_list'),
    path('medals/<slug>/', views.MedalDetailView.as_view(), name='medal_detail'),
    path('map/', views.MapView.as_view(), name='map'),
    path('en/', views.IndexView.as_view(lang='en'), name='index_en'),
    path('nl/', views.IndexView.as_view(lang='nl'), name='index_nl'),
    path('jinja/', views.JinjaTest.as_view(), name='jinja_test'),
    path('gallery/<slug>/', views.GalleryView.as_view(), name='gallery'),
    path('', views.IndexView.as_view(lang='af'), name='index_af'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
