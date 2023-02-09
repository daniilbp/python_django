from django import forms
from app_goods.models import File

class UploadPriceForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file',)


# class UploadPriceForm(forms.Form):
#     file = forms.FileField()
