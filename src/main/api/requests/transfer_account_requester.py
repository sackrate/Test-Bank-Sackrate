from src.main.api.requests.requester import Requester
from src.main.api.models.transfer_account_response import TransferAccountResponse
from src.main.api.models.transfer_account_request import TransferAccountRequest
import requests
from requests import Response
from http import HTTPStatus


class TransferAccountRequester(Requester):
    def post(self, transfer_account_request: TransferAccountRequest)->TransferAccountResponse | Response:
        url=f"{self.base_url}/account/transfer"
        response = requests.post(
            url=url,
            json=transfer_account_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]:
            return TransferAccountResponse(**response.json())
        return response
