from django import forms
from post.models import Post,Comment
from utils.utility import get_or_not_found



class PostCreationForm(forms.Form):
    description = forms.CharField()
    # user = forms.CharField()


    def save(self,commit=True):
        post = Post(description=self.cleaned_data.get("description"))
        return post



class CreatePostCommentForm(forms.Form):
    user = forms.CharField()
    message = forms.CharField()
    post = forms.IntegerField()
    
    def save(self,user):
        post =get_or_not_found(Post.objects.all(),id=self.cleaned_data.get("post"))
        comment = Comment(message =self.cleaned_data.get("message"),post=post,user=user)
        return comment
