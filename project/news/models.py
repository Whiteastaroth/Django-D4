from django.db import models
from django.shortcuts import reverse


class New(models.Model):
    CATEGORIES_CHOICES = [('uncos', 'Новости'), ('articles', 'Статьи')]

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField()
    text = models.TextField()
    data_pub = models.DateTimeField(auto_now_add=True)
    category = models.SlugField(max_length=10, choices=CATEGORIES_CHOICES, default='uncos')


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


    def __str__(self):
        return '{}' .format(self.title)

