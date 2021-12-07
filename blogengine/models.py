from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import time
from django.utils.text import slugify


def slug_generator(string):
    """create a human-readable text for url slug"""
    new_slug = slugify(string, allow_unicode=True)
    return new_slug + '-' + str(int(time.time()))

class Post(models.Model):
    """
    Модели:
    Пост в блоге:
    Title
    Content
    Pub_date
    Upd_date
    Photo/s
    Author
    Tag
    """
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    upd_date = models.DateTimeField(auto_now=True ,verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='images/%Y-%m-%d/', blank=True, verbose_name='Фото')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор поста')
    tag = models.ManyToManyField(to='Tag', blank=True, related_name='posts')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)

    # auto-generating and save slug after creating post
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_generator(self.title)
        super().save(*args, **kwargs)

    # get unique url for unique slug
    def get_absolute_url(self):
        return reverse('detailed_post', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тэг')
    slug = models.SlugField(unique=True, max_length=50, default='', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ('title',)

    def get_absolute_url(self):
        return reverse('detailed_tags', kwargs={'slug': self.slug})