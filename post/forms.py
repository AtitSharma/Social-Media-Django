from django import forms
from post.models import Post



class PostCreationForm(forms.Form):
    description = forms.CharField()
    # user = forms.CharField()


    def save(self,commit=True):
        post = Post(description=self.cleaned_data.get("description"))
        return post



