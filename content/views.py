from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic

from .forms import ImageForm
from .models import Image
from django.contrib.auth.mixins import LoginRequiredMixin


# TODO: check for correct permissions
class BulkImageAdminView(LoginRequiredMixin, generic.View):

    def get(self, request):
        return render(request, 'admin/content_image_bulk.html')

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


class ImageAdminView(generic.View):

    def get(self, request, pk):
        tag = request.GET.get('tag')

        images = Image.objects.filter(tags__contains=[tag])

        image_data = [{
            'id': i.id,
            'src': i.image.thumbnail['400x400'].url
        } for i in images]

        return JsonResponse({
            'ok': True,
            'images': image_data
        })

    def post(self, request, pk):
        form = ImageForm(request.POST, request.FILES)

        if not form.is_valid():
            return JsonResponse({
                'ok': False,
                'errors': form.errors
            })

        obj = form.save()

        return JsonResponse({'ok': True, 'id': obj.id})
