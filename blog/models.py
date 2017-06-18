import time
from django.db import models
from django.utils import timezone
# Create your models here.
class PostModel(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200, verbose_name='Post title')
    body = models.TextField(max_length=5000, verbose_name='Post Text')
    likes = models.IntegerField(default=0, verbose_name='Post likes')
    views = models.IntegerField(default=0, verbose_name='Post views')
    createTime = models.DateTimeField(blank=True,verbose_name='Post create time')
    image = models.ImageField(upload_to='images',verbose_name='Post image')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            if not self.createTime:
                self.createTime = timezone.now()
        return super(PostModel, self).save(*args, **kwargs)

    def __str__(self):
        return 'Post {}'.format(self.title)


class PostCommentModel(models.Model):
    objects = models.Manager()
    userName = models.CharField(max_length=30, verbose_name='User name hwo post comment')
    Email = models.EmailField(max_length=30, verbose_name='User email hwo post comment')
    body = models.TextField(max_length=1000, verbose_name='Comment text')
    likes = models.IntegerField(default=0, verbose_name='Comment likes')
    views = models.IntegerField(default=0, verbose_name='Comment views')
    createTime = models.DateTimeField(blank=True,verbose_name='Comment create time')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "PostComment"
        verbose_name_plural = "PostComments"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            if not self.createTime:
                self.createTime = timezone.now()
        return super(PostCommentModel, self).save(*args, **kwargs)

    def __str__(self):
        return 'Post Comment {}'.format(self.userName)

