from django.urls import reverse
from django.views import generic

from .models import Member, Research, CommitteeMember, Post, Project


class IndexView(generic.TemplateView):
    lang = 'af'

    def get_template_names(self):
        return [f'index_{self.lang}.html']


class ContactView(generic.TemplateView):
    template_name = 'contact.html'


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
    template_name = 'application.html'

    def get_success_url(self):
        return reverse(f'application_success')


class CommitteeView(generic.ListView):
    model = CommitteeMember
    context_object_name = 'members'
    template_name = 'committee.html'
    ordering = ['order']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(active=True)


class LinksView(generic.TemplateView):
    template_name = 'links.html'


class ResearchListView(generic.ListView):
    template_name = 'research_list.html'
    model = Research
    context_object_name = 'researches'


class ApplicationSuccessView(generic.TemplateView):
    template_name = 'application_success.html'



class AboutView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['committee_members'] = CommitteeMember.objects.filter(active=True).order_by('order')

        return ctx


class MembershipView(generic.TemplateView):
    template_name = 'membership.html'

class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'post_detail.html'


class ProjectListView(generic.ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'


class ProjectDetailView(generic.DetailView):
    model = Project
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'project_detail.html'
