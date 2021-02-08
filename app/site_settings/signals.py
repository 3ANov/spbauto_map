from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from site_settings.models import SiteSettings, SocialLink


def clear_site_settings_cache():
    cache.delete('site_settings')


@receiver(post_save, sender=SiteSettings)
def invalidate_site_settings_cache(sender, **kwargs):
    clear_site_settings_cache()


def clear_social_links_cache():
    cache.delete('social_links')


@receiver(post_save, sender=SocialLink)
def invalidate_social_links_cache(sender, **kwargs):
    clear_social_links_cache()
