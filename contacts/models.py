from django.db import models

# Create your models here.

class MyContactModel(models.Model):
    objects = models.Manager()
    phone = models.CharField(null=True,default=None,max_length=20, blank=True,verbose_name='Phone')
    email = models.CharField(max_length=20,null=True,default=None, blank=True, verbose_name='Email')
    address = models.CharField(max_length=50, null=True,default=None, blank=True,verbose_name='Address')
    use = models.BooleanField(default=False, blank=True, verbose_name='In use')
    class Meta:
        verbose_name = "Мої контакти"
        verbose_name_plural = "Мої контакти"

    def __str__(self):
        return '{}, {}, {}'.format(self.phone,self.email,self.address)

class ConnectModel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=25,verbose_name='Name')
    email = models.EmailField(max_length=25, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Phone')
    text = models.TextField(max_length=1000, verbose_name='Text')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Time')
    class Meta:
        verbose_name = "Звернення"
        verbose_name_plural = "Звернення"

    def __str__(self):
        return 'звернення від - {}'.format(self.name)