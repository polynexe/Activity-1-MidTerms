from django.forms import forms
from .models import Tweets
import tweet
from .models import *
from django.core.exceptions import ValidationError


class TweetForm():
    class Meta:
        model = tweet
        fields = ('content', 'image')

    def clean_content(self):
        content = self.cleaned_data['content']
        prohibited_words = ['shit', 'fuck', 'bobo']
        content_lower = content.lower()

        for word in prohibited_words:
            if word.lower() in content_lower.lower():
                raise forms.ValidationError('This word is prohibited!')
            return content