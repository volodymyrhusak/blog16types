from django.forms import ModelForm
from .models import ApplicationProjectModel

class ApplicationProjectForm(ModelForm):
    class Meta:
        model = ApplicationProjectModel
        fields = ['firstName', 'lastName', 'areaCode','telNum','emailId']
