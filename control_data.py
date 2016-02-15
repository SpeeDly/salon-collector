import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawler.settings")
from crawler.beauty_salon.models import Salon
from django.db.models import Q


def delete_duplicate():
    count = 0
    for row in Salon.objects.all():
        if Salon.objects.filter(place_id=row.place_id).count() > 1:
            row.delete()
            count += 1
    print(count, "rows has been deleted")
    return "{count} rows has been deleted".format(count=count)

delete_duplicate()