from django import forms

from .models import Image, validate_tag, TAG_MAX_LENGTH


class ImageForm(forms.ModelForm):

    object_tag = forms.CharField(max_length=TAG_MAX_LENGTH, validators=[validate_tag])

    class Meta:
        model = Image
        fields = [
            'image',
        ]

    def save(self, commit=True):
        instance = super().save(commit=commit)

        object_tag = self.cleaned_data['object_tag']

        if not object_tag:
            # image not linked to an object
            return instance

        current_tags = instance.tags or []

        if object_tag in current_tags:
            # image already linked to an object
            return instance

        instance.tags = current_tags + [object_tag]
        instance.save()
        return instance


class ImageDetailForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = [
            'caption'
        ]
