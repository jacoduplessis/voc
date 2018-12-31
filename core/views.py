from django.urls import reverse
from django.views import generic

from .models import Member


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


class CommitteeView(generic.TemplateView):

    template_name = 'committee.html'

class LinksView(generic.TemplateView):

    template_name = 'links.html'

class ApplicationSuccessView(generic.TemplateView):
    lang = 'en'

    def get_template_names(self):
        return [f'application_success_{self.lang}.html']
