from django import forms
from softTech.models import VideoModel

class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = "__all__"