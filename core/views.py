from django.urls import reverse
from django.views import generic

from .models import Member, Research, CommitteeMember, Post


class IndexView(generic.TemplateView):
    lang = 'af'

    def get_template_names(self):
        return [f'index_{self.lang}.html']


class ContactView(generic.TemplateView):
    lang = 'en'

    def get_template_names(self):
        return [f'contact_{self.lang}.html']


class LogoView(generic.TemplateView):
    template_name = 'logo.html'


class CopyrightPrivacyView(generic.TemplateView):
    template_name = 'copyright_privacy.html'


class ArchiveView(generic.TemplateView):
    template_name = 'archives.html'


class EventListView(generic.TemplateView):
    template_name = 'event_list.html'


class ApplicationView(generic.CreateView):
    lang = 'en'
    model = Member
    fields = [
        'title',
        'name',
        'contact_number',
        'email_address',
    ]

    def get_template_names(self):
        return [f'application_{self.lang}.html']

    def get_success_url(self):
        return reverse(f'application_success_{self.lang}')


class CommitteeView(generic.ListView):
    model = CommitteeMember
    context_object_name = 'members'
    template_name = 'committee.html'
    ordering = ['order']


class LinksView(generic.TemplateView):
    template_name = 'links.html'


class ResearchListView(generic.ListView):
    template_name = 'research_list.html'
    model = Research
    context_object_name = 'researches'


class ApplicationSuccessView(generic.TemplateView):
    lang = 'en'

    def get_template_names(self):
        return [f'application_success_{self.lang}.html']


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'post_detail.html'
