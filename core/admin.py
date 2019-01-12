from django.contrib import admin
from .models import Member, Post, CommitteeMember, Research, PostImage, Document
from django.utils.translation import ugettext_lazy


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
    list_display = ['name', 'position_af', 'position_en', 'email_address_private', 'email_address_public', 'active', 'order']


class ResearchAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'link']


admin.site.register(Member, MemberAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(Document, DocumentAdmin)

admin.site.site_title = ugettext_lazy('Stigting VOC Admin')
admin.site.site_header = ugettext_lazy('Stigting VOC Administration')
admin.site.index_title = ugettext_lazy('Stigting VOC')
