from django.core.cache import cache

from site_settings.models import SiteSettings, SocialLink


def load_settings(request):
    site_settings = cache.get('site_settings')
    social_links = cache.get('social_links')
    if site_settings is None:
        site_settings = SiteSettings.load()
        cache.set('site_settings', site_settings)
    if social_links is None:
        social_links = SocialLink.objects.filter(settings_id=site_settings.id)
        cache.set('social_links', social_links)
    return {'site_settings': site_settings,
            'site_social_link': social_links}
