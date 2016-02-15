import os
import sys
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawler.settings")
from crawler.beauty_salon.models import Salon


Cities = {
    "London": "51.5286417,-0.1015987",
    "Berlin": "52.5075419,13.4261419",
    "Melbourne": "-37.8602828,145.079616", 
    "New York": "40.7056308,-73.9780035",
    "Boston": "42.3133735,-71.0571571",
    "Shanghai": "31.2243489,121.4767528",
    "Manchester": "53.4722454,-2.2235922",
    "Perth": "-31.9795684,115.9185316",
    "Sydney": "-33.7969235,150.9224326",
    "Liverpool": "53.3877518,-2.7618409",
    "Birmingham": "52.4678684,-1.6573267",
    "Southampton": "50.9900009,-1.5998731",
    "Portsmouth": "50.814851,-1.0965218", 
    "Nottingham": "53.1185377,-2.5014048",
    "Newcastle": "55.0023721,-1.6568434",
    "Bristol": "51.468489,-2.5907094",
    "Washington": "38.8935965,-77.014576",
    "Los Angeles": "34.0204989,-118.4117325",
    "Miami": "25.903756,-80.2918482",
    "Las Vegas": "36.125,-115.175",
    "Atlanta": "33.7677129,-84.4206039",
    "Houston": "29.817178,-95.4012915",
    "San Antonio": "29.4814305,-98.5144044",
    "Dallas": "32.8206645,-96.7313396",
    "Phoenix": "33.6054149,-112.125051",
    "Chicago": "42.1542311,-88.1131334",
    "Philadelphia": "40.002498,-75.1180329",
    "Detroit": "42.352711,-83.099205",
    "Cleveland": "41.4949426,-81.70586",
    "Vermont": "43.8717545,-72.4477828",
    "Montreal": "45.5601451,-73.7120832",
    "Quebec": "46.8580074,-71.3460728",
    }

def collect_places(page=10):
    key = "AIzaSyAtiK2OdoAQZCz-JmXJ_M4z3wtJ0ggnllQ"
    query = "hair" # ne e dovursheno !!!
    types = "beauty_salon|hair_care"
    exclude_types = ["doctor", "health"]
    city = "Quebec"
    location = Cities[city]
    page_token = ""

    for i in range(page):
        print("first_request:")
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?key={key}&query={query}&types={types}&location={location}&radius=50000&pagetoken={page_token}'.format(key=key, query=query, types=types, location=location, page_token=page_token)
        request = requests.get(url)
        result_json = request.json()
        results = result_json["results"]

        for r in results:
            flag = False
            types = r["types"]
            place_id = r["place_id"]
            for temp in types:
                if temp in exclude_types:
                    flag = True
            try:
                Salon.objects.get(place_id=place_id)
                flag = True
            except:
                pass

            if not flag:
                
                name = r["name"]
                formatted_address = r["formatted_address"]
                try:
                    lat = r["geometry"]["location"]["lat"]
                    lng = r["geometry"]["location"]["lng"]
                except:
                    lat = None
                    lng = None
                print("second_request:")
                url_place = "https://maps.googleapis.com/maps/api/place/details/json?key={key}&placeid={place_id}".format(key=key, place_id=place_id)
                request_place = requests.get(url_place)
                temp_json = request_place.json()
                place_results = temp_json["result"]
                try:
                    formatted_phone_number = place_results["formatted_phone_number"]
                    international_phone_number = place_results["international_phone_number"]
                except:
                    formatted_phone_number = None
                    international_phone_number = None
                    print(sys.exc_info()[0])
                try:
                    website = place_results["website"]
                except:
                    website = None
                try:
                    rating = float(place_results["rating"])
                except:
                    rating = None
                try:
                    rated = int(place_results["user_ratings_total"])
                except:
                    rated = None
                
                address_components = place_results["address_components"]
                try:
                    for component in address_components:
                        # if "administrative_area_level_1" in component["types"] or "administrative_area_level_2" in component["types"] or "locality" in component["types"]:
                        #     city = component["long_name"] 
                        if "country" in component["types"]:
                            country = component["short_name"]
                except:
                    country = None

                try:
                    Salon.objects.get(place_id=place_id)
                except:
                    Salon.objects.create(
                                    place_id=place_id, 
                                    name=name, 
                                    types=types, 
                                    formatted_phone_number=formatted_phone_number, 
                                    international_phone_number=international_phone_number, 
                                    website=website, 
                                    emails=None, 
                                    formatted_address=formatted_address, 
                                    lng=lng, 
                                    lat=lat, 
                                    city=city, 
                                    country=country, 
                                    rating=rating, 
                                    rated=rated
                                    )

        print(page_token)
        page_token = result_json["next_page_token"]

collect_places(page=10)