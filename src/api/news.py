from fastapi import APIRouter

from module import httprequest
from schema.request import CrawlingRequest

router = APIRouter()


@router.post("/news", status_code=200)
def get_html_handler(
        request: CrawlingRequest,
) -> str:
    response = httprequest.get_http_html(request.url, request.params)
    return response

