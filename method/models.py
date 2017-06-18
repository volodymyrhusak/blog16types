from django.db import models

# Create your models here.

class MethodInUseModel(models.Model):
    objects = models.Manager()
    text = models.CharField(max_length=200, verbose_name='Text')
    use = models.BooleanField(default=False,  blank=True,verbose_name='In use')
    parent = models.ForeignKey('self',null=True, blank=True)
    class Meta:
        verbose_name = "Використовується"
        verbose_name_plural = "Використовується"

    def __str__(self):
        return '{}'.format(self.text)
