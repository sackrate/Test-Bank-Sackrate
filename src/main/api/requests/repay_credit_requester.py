from src.main.api.models.repay_credit_request import RepayCreditRequest
from src.main.api.requests.requester import Requester
from src.main.api.models.repay_credit_response import RepayCreditResponse
import requests
from requests import Response
from http import HTTPStatus

class RepayCreditRequester(Requester):
    def post(self, repay_credit_request: RepayCreditRequest) -> RepayCreditResponse | Response:
        url=f"{self.base_url}/credit/repay"
        response = requests.post(
            url=url,
            json=repay_credit_request.model_dump(),
            headers = self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return RepayCreditResponse(**response.json())
        return response

