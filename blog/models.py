from django.db import models


# Create your models here.
class PostManager(models.Manager):
    def title_content(self, kv):
        return self.filter(title__contains=kv)
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=0)


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    body = models.TextField(verbose_name="内容")
    objects = PostManager()
    is_delete = models.BooleanField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"