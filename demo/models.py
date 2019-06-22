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


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=30)
    sex = models.BooleanField(default=0)
    email = models.EmailField(default="123@gmail.com")
    birthday = models.DateTimeField(auto_now_add=True)
    hobby = models.CharField(max_length=100, default="play ball")
    grade = models.ForeignKey("Grade")

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=50)
    boy_num = models.PositiveIntegerField(default=30)
    girl_num = models.PositiveIntegerField(default=20)
    created_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=100)


class IDCard(models.Model):
    id_num = models.CharField(max_length=18)
    people = models.OneToOneField(People, on_delete=models.PROTECT)


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    body = models.TextField(verbose_name="内容")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"