from src.main.api.models.request_credit_request import RequestCreditRequest
from src.main.api.requests.requester import Requester
from src.main.api.models.request_credit_response import RequestCreditResponse
import requests
from requests import Response
from http import HTTPStatus

class RequestCreditRequester(Requester):
    def post(self, request_credit_request: RequestCreditRequest) -> RequestCreditResponse | Response:
        url=f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            json=request_credit_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return RequestCreditResponse(**response.json())
        return response