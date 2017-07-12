# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class ProjectModel(models.Model):
    objects = models.Manager()
    text = models.CharField(max_length=300, verbose_name='Category name')
    use = models.BooleanField(default=False, blank=True, verbose_name='In use')
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Проекти"

    def __str__(self):
        return 'Проект {}'.format(self.text)

class IUseCategoryModel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name='Category name')
    use = models.BooleanField(default=False, blank=True, verbose_name='In use')
    class Meta:
        verbose_name = "Я використовую категорію"
        verbose_name_plural = "Я використовую категорії"

    def __str__(self):
        return 'Я використовую категорія {}'.format(self.name)


class IUseModel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name='name')
    descr = models.CharField(max_length=200, verbose_name='Description')
    link = models.URLField( blank=True, null=True, verbose_name='Link')
    use = models.BooleanField(default=False, blank=True,verbose_name='In use')
    category = models.ForeignKey(IUseCategoryModel, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Я використовую"
        verbose_name_plural = "Я використовую"

    def __str__(self):
        return 'Я використовую {}'.format(self.name)

class AboutMeModel(models.Model):
    objects = models.Manager()
    slogan = models.CharField(max_length=200, verbose_name='Slogan')
    use = models.BooleanField(default=False,blank=True, verbose_name='In use')
    text = models.TextField(max_length=3000, verbose_name='Text')
    time = models.DateTimeField(auto_now_add=True,blank=True, verbose_name='Time')

    class Meta:
        verbose_name = "Про мене"
        verbose_name_plural = "Про мене"

    def __str__(self):
        return 'Про мене'


class ApplicationProjectModel(models.Model):
    objects = models.Manager()
    firstName = models.CharField(max_length=50, verbose_name='First Name')
    lastName = models.CharField(max_length=50, verbose_name='Last Name')
    time = models.DateTimeField(auto_now_add=True,blank=True, verbose_name='Application time')
    areaCode = models.IntegerField(verbose_name='Area code')
    telNum = models.IntegerField(verbose_name='Phone')
    emailId = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Заявка на "Ознайомча лекція з практичною начинкою"'
        verbose_name_plural = 'Заявки на "Ознайомча лекція з практичною начинкою"'

    def __str__(self):
        return 'Заявка від  %s %s' % (self.firstName, self.lastName)


class BooksModel(models.Model):
    objects = models.Manager()
    author = models.CharField(max_length=25, verbose_name='Author')
    bookName = models.CharField(max_length=50, verbose_name='Book Name')
    time = models.DateTimeField(auto_now_add=True, blank=True,verbose_name='Time')

    class Meta:
        verbose_name = "Моя книга"
        verbose_name_plural = "Мої книги"

    def __str__(self):
        return '%s "%s"' % (self.author, self.bookName)


