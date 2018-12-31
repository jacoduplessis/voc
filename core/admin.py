from django.contrib import admin
from .models import Member, Post


class MemberAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'contact_number', 'email_address', 'state']
    list_filter = ['state']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_published']


admin.site.register(Member, MemberAdmin)
admin.site.register(Post, PostAdmin)
