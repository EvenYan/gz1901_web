from django.db import models

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=50)
    money = models.PositiveIntegerField()
    get_money = models.PositiveIntegerField(default=300)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    passwd = models.CharField(max_length=400)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.username