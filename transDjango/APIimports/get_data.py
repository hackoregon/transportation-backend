import requests
import logging
from APIimports import constants
from APIimports.models import ApiElement

logger = logging.getLogger(__name__)



def oneRingToBindThem():
    for name, url in constants.APIS:
        response = requests.get(url)

        try:
            response.raise_for_status()
            geojson = response.json()

            for element in geojson:
                apiElement = ApiElement(
                        payload=element,
                        url=url,
                        name=name
                )
                apiElement.save()
        # except HTTPError:
        #     logger.exception("non 200 response from api request " + url)
        # except ValueError:
        #     logger.exception("exception parsing json in response from api request against " + url)

        except Exception as e:
            print(e)


