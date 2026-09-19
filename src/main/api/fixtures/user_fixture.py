import pytest

from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.repay_credit_request import RepayCreditRequest
from src.main.api.models.request_credit_request import RequestCreditRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.generators.model_generator import RandomModelGenerator


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_credit_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateCreditUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_account_response(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)

@pytest.fixture
def create_two_account_response(api_manager, create_user_request):
    return api_manager.user_steps.create_account(create_user_request)

@pytest.fixture
def create_credit_account_response(api_manager, create_credit_user_request):
    return api_manager.user_steps.create_account(create_credit_user_request)

@pytest.fixture
def request_credit_response(api_manager, create_credit_user_request,request_credit_request):
    return api_manager.user_steps.request_credit(create_credit_user_request,request_credit_request)


@pytest.fixture
def deposit_account_request(create_account_response):
    return DepositAccountRequest(accountId=create_account_response.id,amount=2000)

@pytest.fixture
def deposit_account_invalid_request(create_account_response):
    return DepositAccountRequest(accountId=create_account_response.id,amount=9999)

@pytest.fixture
def deposit_account_transfer_request(create_account_response):
    for amount in [9000, 2000]:
        return DepositAccountRequest(accountId=create_account_response.id,amount=amount)

@pytest.fixture
def request_credit_request(create_credit_account_response):
    return RequestCreditRequest(accountId=create_credit_account_response.id, amount=6000, termMonths=12)

@pytest.fixture
def request_credit_invalid_request(create_credit_account_response):
    return RequestCreditRequest(accountId=create_credit_account_response.id, amount=1500, termMonths=12)

@pytest.fixture
def repay_credit_request(create_credit_account_response,request_credit_response):
    return RepayCreditRequest(creditId=request_credit_response.creditId, accountId=create_credit_account_response.id, amount = 6000)

@pytest.fixture
def repay_credit_invalid_request(create_credit_account_response,request_credit_response):
    return RepayCreditRequest(creditId=request_credit_response.creditId, accountId=create_credit_account_response.id, amount = 1500)

@pytest.fixture
def transfer_account_invalid_request(create_account_response, create_two_account_response,request):
    return TransferAccountRequest(fromAccountId=create_account_response.id, toAccountId=create_two_account_response.id, amount=request.param)

@pytest.fixture
def transfer_account_request(create_account_response, create_two_account_response):
    return TransferAccountRequest(fromAccountId=create_account_response.id, toAccountId=create_two_account_response.id, amount=1500)