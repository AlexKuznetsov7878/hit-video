from django import forms
from . import models

class CreateVideo(forms.ModelForm):
    class Meta:
        model = models.Video
        fields = ["name", "video_file", "audio_file", "slug", "whisper_transcribe", "whisper_summary"]
        widgets = {'slug': forms.HiddenInput(), "audio_file": forms.HiddenInput(),
                   "whisper_transcribe": forms.HiddenInput(), "whisper_summary": forms.HiddenInput()}
