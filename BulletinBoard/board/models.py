from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Post(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemasters', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmasters', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = RichTextUploadingField()
    files = models.FileField(upload_to='uploads/', blank=True)
    category = models.CharField(max_length=24, choices=TYPE, default='tank')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('board')


class Response(models.Model):
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=128)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'

    def get_absolute_url(self):
        return reverse('board')
