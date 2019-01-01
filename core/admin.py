from django.contrib import admin
from .models import Member, Post, CommitteeMember, Research, PostImage


class PostImageInline(admin.StackedInline):
    model = PostImage
    fields = ['image', 'caption']


class MemberAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'contact_number', 'email_address', 'state']
    list_filter = ['state']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'date_published']
    inlines = [
        PostImageInline
    ]
    list_editable = ['slug']


class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position_af', 'position_en', 'order']


class ResearchAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'link']


admin.site.register(Member, MemberAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
