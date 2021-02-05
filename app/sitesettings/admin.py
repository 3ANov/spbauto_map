from django.contrib import admin

# Register your models here.
from app.sitesettings.models import SiteSettings
from app.sitesettings.models import SocialLink


class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    extra = 1


class GeneralSiteSetting(admin.ModelAdmin):
    inlines = [SocialLinkInline]


admin.site.register(SiteSettings,GeneralSiteSetting)