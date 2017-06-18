from django.db import models

# Create your models here.

class AdviceCategoryModel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name='Advice category name')
    use = models.BooleanField(default=False, blank=True, verbose_name='In use')
    class Meta:
        verbose_name = "Катерія консультування"
        verbose_name_plural = "Категорії консультування"

    def __str__(self):
        return 'Категорія консультування {}'.format(self.name)


class AdviceModel(models.Model):
    objects = models.Manager()
    text = models.CharField(max_length=200, verbose_name='Text')
    use = models.BooleanField(default=False,blank=True, verbose_name='In use')
    category = models.ForeignKey(AdviceCategoryModel , on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Консультація"
        verbose_name_plural = "Консультації"

    def __str__(self):
        return 'Консультація: {}'.format(self.text)


class CourseModel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name='Course name')
    descr = models.TextField(max_length=300, verbose_name='Description')
    descrBelow = models.TextField(max_length=300, verbose_name='Description below')
    link = models.URLField(default= None, verbose_name='Download link')
    use = models.BooleanField(default=False,blank=True, verbose_name='In use')
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"

    def __str__(self):
        return 'Курс {}'.format(self.name)


class OnCourseModel(models.Model):
    objects = models.Manager()
    text = models.CharField(max_length=200, verbose_name='Text')
    use = models.BooleanField(default=False,blank=True, verbose_name='In use')
    category = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "На курсі"
        verbose_name_plural = "На курсі"

    def __str__(self):
        return '{}'.format(self.text)
