from django.db.models import Q
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.models import User, Group

from crawler.beauty_salon.models import Salon
from crawler.beauty_salon.export_csv import export_as_csv_action
from crawler.settings import COUNTRY

admin.autodiscover()


class EmailsFilter(SimpleListFilter):
    title = 'Emails'

    parameter_name = 'emails'

    def lookups(self, request, model_admin):
        return ((0, "Have emails"), (1, "Don't have emails"),)

    def queryset(self, request, queryset):
        if self.value() == "0":
            return queryset.filter(~Q(emails="[]"), ~Q(emails=None))
        elif self.value() == "1":
            return queryset.filter(Q(emails="[]")|Q(emails=None))


class WebsiteFilter(SimpleListFilter):
    title = 'Website'

    parameter_name = 'website'

    def lookups(self, request, model_admin):
        return ((0, "Have website"), (1, "Don't have website"),)

    def queryset(self, request, queryset):
        if self.value() == "0":
            return queryset.filter(~Q(website=None))
        elif self.value() == "1":
            return queryset.filter(website=None)


class SalonAdmin(admin.ModelAdmin):
    list_display = ("name", "international_phone_number", "salon_link", "emails", "formatted_address", "city", "country", "called", "mailed")
    list_filter = (WebsiteFilter, EmailsFilter, ('mailed', admin.BooleanFieldListFilter), ('called', admin.BooleanFieldListFilter), "city", "country",)
    search_fields = ("name", "emails", "website",)
    list_editable = ("called", "mailed")
    actions = [export_as_csv_action("CSV Export", fields=["place_id", "name", "types", "formatted_phone_number", "international_phone_number", "website", "emails", "formatted_address", "lng", "lat", "country", "city", "rating", "rated", "called", "mailed", "note"])]

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Salon, SalonAdmin)