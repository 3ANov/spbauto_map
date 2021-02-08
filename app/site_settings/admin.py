from django.contrib import admin

# Register your models here.
from site_settings.models import SiteSettings
from site_settings.models import SocialLink


class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    extra = 1


class GeneralSiteSetting(admin.ModelAdmin):
    inlines = [SocialLinkInline]


admin.site.register(SiteSettings,GeneralSiteSetting)