from django.core.cache import cache
from django.db import models

# Create your models here.


class SingletonModel(models.Model):
    """ Синглтон-модель """

    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete()

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class SiteSettings(SingletonModel):
    """ Модель для хранения настроек сайта """

    title = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=200, blank=True)
    address = models.TextField(blank=True)
    telephone_number = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = "Основные настройки сайта"


class SocialLink(models.Model):
    """ Модель для хранения ссылок на соц.сети """

    settings = models.ForeignKey(SiteSettings, on_delete=models.SET_DEFAULT, default=1)
    link = models.URLField()
    icon = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Ссылки на социальные сети"
