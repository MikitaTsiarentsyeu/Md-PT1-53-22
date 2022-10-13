from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100, label="Title of the post")
    subtitle = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':"text-area"}))
    image = forms.ImageField(label="Main image")
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)

    def clean_subtitle(self):

        title_data = self.cleaned_data['title']
        subtitle_data = self.cleaned_data['subtitle']

        if title_data == subtitle_data:
            raise ValidationError("The title and subtitle should not be the same")

        return subtitle_data


class AddModelPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'post_type', 'image')