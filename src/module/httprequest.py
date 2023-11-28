import requests
from urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup

import logging
from schema.request import Params
logger = logging.getLogger(__name__)


def get_http_html(
        url: str,
        params: Params
) -> str:
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    params = dict(params)
    response = requests.get(url, params=params, verify=False)
    html = response.text
    # logger.debug("Http status %s", response.status_code)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

    return soup.contents


