import os
import re
import requests
from urllib.parse import urljoin
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawler.settings")

from crawler.beauty_salon.models import Salon


def crawling():
    email_re = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
    link_re = re.compile(r'href="(.*?)"')

    def crawl(root, url, maxlevel):

        if maxlevel == 0 or len(url.split(root)) == 1:
            return []

        try:
            req = requests.get(url, timeout=5)
            result = []

            if(req.status_code != 200):
                return []
        except:
            return []


        links = link_re.findall(req.text)
        for link in links:
            link = urljoin(url, link)
            result += crawl(root, link, maxlevel - 1)

        result += email_re.findall(req.text)

        return result

    salons = Salon.objects.filter(emails=None, crawled=False).exclude(website=None)
    _all = Salon.objects.filter(emails=None).exclude(website=None).count()

    for i,salon in enumerate(salons):
        url = root = salon.website
        print("{0}/{1}".format(i,_all), salon.website)
        emails = crawl(root, url, 2)
        emails = set(emails)
        emails = list(emails)
        salon.emails = emails
        salon.save()


crawling()
