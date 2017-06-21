from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import BooksModel, AboutMeModel, IUseCategoryModel, IUseModel, ProjectModel
from django.core.mail import EmailMessage
from .forms import ApplicationProjectForm
from contacts.models import MyContactModel
from django.conf import settings


EMAIL_TITLE = 'Заявка на ознайомчу лекцію від {0} {1}'
EMAIL_TEXT = '''Ви получили нову заявку на ознайомчу лекцію від {0} {1} 
Телевон: {2} {3}
Email: {4}'''

def aboutMe(request):
    me = AboutMeModel.objects.get(use=1)
    context = {'me':me}
    return render(request, 'aboutMe.html',context)

def aboutUse(request):
    categories = IUseCategoryModel.objects.filter(use=True)
    use = IUseModel.objects.filter(category__in=categories)
    context = {'use':use,
               'categories':categories}
    return render(request, 'aboutUse.html', context)

@csrf_protect
def aboutProjects(request):
    projects = ProjectModel.objects.filter(use=True)
    context = {'projects': projects}

    if request.POST:
        form = ApplicationProjectForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            sendEmail = MyContactModel.objects.get(use=True).email
            email = EmailMessage(EMAIL_TITLE.format(data['firstName'], data['lastName']),
                                 EMAIL_TEXT.format(data['firstName'],
                                                   data['lastName'],
                                                   data['areaCode'],
                                                   data['telNum'],
                                                   data['emailId']),
                                 to=[sendEmail])
            # email.send()
        else:
            context.update({'formErrors': form})

    return render(request, 'aboutProjects.html',context)


def aboutBooks(request):
    books = BooksModel.objects.all()
    context ={'books': books}
    return render(request, 'aboutBooks.html',context)


def aboutResponse(request):
    # if request.POST:
    #     print('POST')
    #     form = ResponseModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    # if request.is_ajax():
    #     print('is_ajax')
    #     return render(request, 'aboutResponse.html')
    #
    # responses = ResponseModel.objects.filter(parentResponse=None)
    # print(len(responses))
    # context = {
    #     'responses':responses,
    #     'countResponses':len(responses)
    # }
    return render(request, 'aboutResponse.html')
