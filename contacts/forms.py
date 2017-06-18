from django.forms import ModelForm
from .models import ConnectModel

class ConnectModelForm(ModelForm):
    class Meta:
        model = ConnectModel
        fields = ['name', 'email', 'phone','text']
