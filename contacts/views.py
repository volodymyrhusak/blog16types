from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import MyContactModel
from .forms import ConnectModelForm
from django.core.mail import EmailMessage
from django.conf import settings

EMAIL_TITLE = 'Від 16TYPES з вами хочуть контактувати'
EMAIL_TEXT = '''Доброго дня Павло :)
на сайті з вами хочуть контактувати:
Ім'я: {}
Телефон: {}
Email: {}
Коментар: {}'''


# Create your views here.
@csrf_protect
def contacts(request):
    contacts = MyContactModel.objects.get(use=True)
    context = {'contacts': contacts}
    if request.POST:
        form = ConnectModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            sendEmail = MyContactModel.objects.get(use=True).email
            email = EmailMessage(EMAIL_TITLE,
                                 EMAIL_TEXT.format(data['name'],
                                                   data['phone'],
                                                   data['email'],
                                                   data['text']),
                                 to=[sendEmail])
            # email.send()
        else:
            context.update({'formErrors': form})

    return render(request, 'contacts.html',context)