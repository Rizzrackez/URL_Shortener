from django.db import models


class SourceURL(models.Model):
    """Модель сокращения URL"""
    url = models.CharField(verbose_name='URL источника', max_length=256)
    slug = models.SlugField(verbose_name='Сокращенный URL')

    def __str__(self):
        return f'Source [{self.slug}] with id [{self.id}].'

    class Meta:
        db_table = 'url_shorterer_object'




