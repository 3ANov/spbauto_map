import locationiq

from django.conf import settings
from locationiq import ApiException

from problem_register.models import ProblemLabel


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
                                            normalizecity=0,
                                            addressdetails=1)
        print(api_response.address)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->autocomplete: %s\n" % e)
