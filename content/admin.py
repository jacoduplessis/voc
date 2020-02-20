from django.contrib import admin
from django.urls import path
from django.utils.html import mark_safe

from .models import Document, Image
from .views import BulkImageAdminView, ImageAdminView


def thumbnail_list_display(size):
    def image(obj):
        if not obj.image:
            return ''
        return mark_safe('<img src="{}" style="max-width:100%">'.format(obj.image.thumbnail[f'{size}x{size}'].url))

    return image


def crop_list_display(size):
    def image(obj):
        if not obj.image:
            return ''
        return mark_safe('<img src="{}" style="max-width:100%">'.format(obj.image.crop[f'{size}x{size}'].url))

    return image


class ImageManagementAdmin:
    change_form_template = 'admin/change_form_with_images.html'

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path('<int:pk>/images/', ImageAdminView.as_view(), name='content_image'),
        ]

        return custom + urls




class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'time_created'
    search_fields = ['image', 'caption', 'tags']
    change_list_template = 'admin/content_image_change_list.html'

    list_display = [
        crop_list_display(80),
        'image',
        'caption',
        'time_created',
        'tags',
    ]
    readonly_fields = [
        thumbnail_list_display(800)
    ]
    list_editable = [
        'caption',
        'tags',
    ]

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path('bulk/', BulkImageAdminView.as_view(), name='content_image_bulk'),
        ]

        return custom + urls


# class GalleryAdmin(admin.ModelAdmin):
#     list_display = [
#         '__str__',
#         'account_actions',
#     ]
#
#     readonly_fields = [
#         'gallery_images',
#         'account_actions',
#     ]
#
#     change_form_template = 'admin/change_form_with_images.html'
#
#     def account_actions(self, obj):
#         return format_html(
#             '<a class="button" href="{}">Upload</a>&nbsp;',
#             reverse('admin:content_gallery_image_upload', args=[obj.pk]),
#         )
#
#     account_actions.short_description = 'Gallery Actions'
#     account_actions.allow_tags = True
#
#     def gallery_images(self, obj):
#         return ', '.join([str(i.image.image) for i in obj.images.all().select_related('image')])
#
#     def get_urls(self):
#         urls = super().get_urls()
#         custom = [
#             path('<int:pk>/upload/', GalleryImageUploadAdminView.as_view(), name='content_gallery_image_upload'),
#         ]
#
#         return custom + urls


class DocumentAdmin(ImageManagementAdmin, admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)
admin.site.register(Document, DocumentAdmin)
