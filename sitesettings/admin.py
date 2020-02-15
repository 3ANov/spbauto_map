from django.contrib import admin

# Register your models here.
from sitesettings.models import SiteSettings
from sitesettings.models import SocialLink


class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    extra = 1


class GeneralSiteSetting(admin.ModelAdmin):
    inlines = [SocialLinkInline]


admin.site.register(SiteSettings,GeneralSiteSetting)