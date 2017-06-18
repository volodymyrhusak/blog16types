from django.contrib import admin
from .models import PostCommentModel,PostModel

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','body', 'likes', 'views','createTime')

class PostCommentModelAdmin(admin.ModelAdmin):
    list_display = ('userName','Email','body', 'likes', 'views','createTime')

admin.site.register(PostModel,PostModelAdmin)
admin.site.register(PostCommentModel,PostCommentModelAdmin)