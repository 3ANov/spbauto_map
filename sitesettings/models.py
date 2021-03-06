from django.core.cache import cache
from django.db import models

# Create your models here.


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class SiteSettings(SingletonModel):
    title = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=200, blank=True)
    address = models.TextField(blank=True)
    telephone_number = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = "Основные настройки сайта"


class SocialLink(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.SET_DEFAULT, default=1)
    link = models.URLField()
    icon = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Ссылки на социальные сети"
