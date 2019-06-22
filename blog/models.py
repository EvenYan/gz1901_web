from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    body = models.TextField(verbose_name="内容")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"