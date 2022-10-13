from django.db import models
from django.utils.safestring import mark_safe

class Photo(models.Model):
    path = models.ImageField(null=True, blank=True, verbose_name='Фото')
    publication_date = models.DateTimeField(verbose_name='Дата публикации')

    def path_tag(self):
        if self.path:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.path.url)
        else:
            return 'No Image Found'
    path_tag.short_description = 'Image'
    


class Fishing(models.Model):
    """Модель описания  в базе данных"""

    latitude = models.FloatField(max_length=200, verbose_name='Долгота')
    longitude = models.FloatField(max_length=200, verbose_name='Широта')
    photos = models.ManyToManyField(Photo, related_name='photos')
    trophies = models.CharField(max_length=100, verbose_name='Трофей')
    description = models.CharField(max_length=255, verbose_name='Описание места')
    publication_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    tackle = models.CharField(max_length=255, verbose_name='Снасти')    
    bait = models.CharField(max_length=255, verbose_name='Наживки')    
    boat = models.CharField(max_length=255, verbose_name='Лодка')
    motor = models.CharField(max_length=255, verbose_name='Мотор')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')



class PartnerLink(models.Model):
    """Модель описания партнёров в базе данных"""

    title = models.CharField(max_length=100, db_index=True, verbose_name='Имя партнёра')
    url = models.URLField(max_length=255)
    publication_date = models.DateTimeField(verbose_name='Дата публикации')



class Shop(models.Model):
    """Модель описания  ссылок партнерских магазинов в базе данных"""

    title = models.CharField(max_length=100, db_index=True, verbose_name='Имя партнёра')
    url = models.URLField(max_length=255)
    publication_date = models.DateTimeField(verbose_name='Дата публикации')
