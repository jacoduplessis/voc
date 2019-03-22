from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy

from content.admin import ImageManagementAdmin
from .models import Member, Post, CommitteeMember, Research, PostImage, Document, Project, Medal, Tour, Event, \
    Newsletter


class PostImageInline(admin.StackedInline):
    model = PostImage
    fields = ['image', 'caption']


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_published', 'time_created']


class MemberAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'contact_number', 'email_address', 'date_joined', 'state']
    list_filter = ['state']
    search_fields = ['name', 'email_address', 'contact_number']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'date_published']
    inlines = [
        PostImageInline
    ]
    search_fields = ['title', 'content']


class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position_af', 'position_en', 'email_address_private', 'email_address_public', 'active',
                    'order']


class ResearchAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'link']


class ProjectAdmin(ImageManagementAdmin, admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'timeline',
        'short_description'
    ]


class MedalAdmin(ImageManagementAdmin, admin.ModelAdmin):
    list_display = [
        'name',
        'date',
        'short_description',
    ]


def thumbnail(size):
    def image(obj):
        return mark_safe('<img src="{}" style="max-width:100%">'.format(obj.image.crop[f'{size}x{size}'].url))

    return image


def tags(obj):
    return mark_safe('<code>{}</code>'.format(', '.join(obj.tags)))


class TourAdmin(ImageManagementAdmin, admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


class NewsletterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Member, MemberAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Medal, MedalAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Newsletter, NewsletterAdmin)

admin.site.site_title = ugettext_lazy('Stigting VOC Admin')
admin.site.site_header = ugettext_lazy('Stigting VOC Administration')
admin.site.index_title = ugettext_lazy('Stigting VOC')
