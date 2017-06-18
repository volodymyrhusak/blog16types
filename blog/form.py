from django.forms import ModelForm
from .models import PostCommentModel

class PostCommentModelForm(ModelForm):
    class Meta:
        model = PostCommentModel
        fields = ['userName', 'Email', 'body']
