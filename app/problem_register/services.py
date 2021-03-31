import logging

import locationiq

from django.conf import settings
from locationiq import ApiException

from places.models import Road, StateDistrict, County, Place
from problem_register.models import ProblemLabel

logger = logging.getLogger(__name__)


def add_places_info_for_problem(problem_pk):
    problem = ProblemLabel.objects.get(pk=problem_pk)

    configuration = locationiq.Configuration()
    configuration.api_key['key'] = settings.REVERSE_GEOCODING_API_KEY
    configuration.host = settings.REVERSE_GEOCODING_API_URL

    with locationiq.ApiClient(configuration) as api_client:
        api_instance = locationiq.ReverseApi(api_client)

    try:
        api_response = api_instance.reverse(lat=problem.geom.y,
                                            lon=problem.geom.x,
                                            accept_language='ru',
                                            format='json',
                                            normalizecity=1,
                                            namedetails=1,
                                            addressdetails=1,
                                            )
        logger.info(api_response.address)

        if api_response.address.road:
            problem.road, _ = Road.objects.get_or_create(name=api_response.address.road)

        if api_response.address.state_district:
            problem.state_district, _ = StateDistrict.objects.get_or_create(name=api_response.address.state_district)

        if api_response.address.county:
            problem.county, _ = County.objects.get_or_create(name=api_response.address.county)

        if api_response.address.house_number:
            problem.house_number = api_response.address.house_number

        if api_response.address.hamlet:
            problem.place, _ = Place.objects.get_or_create(name=api_response.address.hamlet)
        elif api_response.address.town:
            problem.place, _ = Place.objects.get_or_create(name=api_response.address.town)
        elif api_response.address.state == "Санкт-Петербург":
            problem.place, _ = Place.objects.get_or_create(name="Санкт-Петербург")

        problem.save()
    except ApiException as e:
        print("Exception when calling ReverseApi->reverse: %s\n" % e)
