from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.http.response import JsonResponse

from .models import Member, Research, CommitteeMember, Post, Project, Medal, Tour, Speaker, Image
from django.core.mail import send_mail
from django_countries.fields import Country
import logging
from .forms import ImageForm

logger = logging.getLogger(__name__)


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
        'country',
        'contact_number',
        'email_address',
        'notes',
    ]
    template_name = 'application.html'

    def get_success_url(self):
        return reverse(f'application_success')

    def form_valid(self, form):

        message = ""
        for key, val in form.cleaned_data.items():
            message += f"{key}: {val}\n"

        country_code = form.cleaned_data.get('country')
        if country_code:
            country = Country(code=country_code)
            message += f"country_name: {country.name}\n"

        logger.info(f"New member: {message}")

        send_mail(
            subject="New Membership Application",
            message=message,
            from_email="Stigting VOC Website <web@voc-kaap.org>",
            recipient_list=[
                'web@voc-kaap.org',
                'sekretaris@voc-kaap.org',
            ],
            fail_silently=True
        )

        return super().form_valid(form)


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


class MapView(generic.TemplateView):
    template_name = 'map.html'


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


class MedalListView(generic.ListView):
    model = Medal
    template_name = 'medal_list.html'
    context_object_name = 'medals'
    ordering = ['date']


class MedalDetailView(generic.DetailView):
    model = Medal
    template_name = 'medal_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class SpeakerListView(generic.ListView):
    model = Speaker
    template_name = 'speaker_list.html'
    context_object_name = 'speakers'


class TourListView(generic.ListView):
    model = Tour
    template_name = 'tour_list.html'
    context_object_name = 'tours'


class TourDetailView(generic.DetailView):
    model = Tour
    template_name = 'tour_detail.html'


class JinjaTest(generic.TemplateView):
    template_name = 'core/test.html'
    template_engine = 'jinja'

    def get_context_data(self, **kwargs):
        from .trello import TBoard
        from pathlib import Path
        import json

        context = super().get_context_data(**kwargs)

        data_str = Path('/home/jaco/Projects/voc/DPZfm02g.json').read_text()
        data = json.loads(data_str)
        context['board'] = TBoard(data=data)
        return context


class GalleryView(generic.TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs.get('slug')

        name = ' '.join([s.capitalize() for s in slug.split('_')])

        context['name'] = name
        context['images'] = Image.objects.filter(tags__contains=[slug])
        return context


class BulkImageAdminView(generic.View):

    def get(self, request):
        return render(request, 'admin/image_bulk.html')

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return JsonResponse({'ok': True, 'id': obj.id})

        else:
            return JsonResponse({
                'ok': False,
                'errors': form.errors
            })
