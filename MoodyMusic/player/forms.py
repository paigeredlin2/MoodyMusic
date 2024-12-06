from django import forms
from .models import Feedback, Song


class FeedbackForm(forms.ModelForm):
    request_user_email = forms.EmailField(label='Your Email')
    request_song = forms.CharField(label="Song Name:", required=False)
    request_artist = forms.CharField(label="Song Artist:", required=False)
    request_remarks = forms.CharField(label="Remarks:", required=False)
    class Meta:
        model = Feedback
        fields = ['request_user_email', 'request_song', 'request_artist', 'request_remarks']