from django.apps import AppConfig


class SiteSettingsConfig(AppConfig):
    name = 'site_settings'

    def ready(self):
        import site_settings.signals
