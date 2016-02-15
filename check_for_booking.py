import os
import re
import requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawler.settings")

from crawler.beauty_salon.models import Salon


def check_for_booking():
    salons = Salon.objects.all().exclude(website=None)
    salons = [s.website for s in salons]
    _all = len(salons)
    booking_re = re.compile(r'(.*)?(buchen)(.*)?')
    counter = 0
    for s in salons:
        try:
            print('{0}/{1}'.format(counter,_all))
            req = requests.get(s)
            booking = booking_re.findall(req.text)
            count = len(booking)
            if count > 0:
                print(s, count)
            counter += 1
        except:
            pass

check_for_booking()