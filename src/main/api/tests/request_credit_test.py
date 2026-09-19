import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.request_credit_request import RequestCreditRequest
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit


@pytest.mark.api
class TestRequestCreditAccount:
    def test_deposit_account_valid(self,db_session: Session,api_manager: ApiManager,create_credit_user_request: CreateCreditUserRequest,request_credit_request: RequestCreditRequest):
        response = api_manager.user_steps.request_credit(create_credit_user_request,request_credit_request)


        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)
        assert credit_from_db.id == response.creditId, "Кредит не получен, id кредита нет в БД"



    def test_deposit_account_invalid(self,db_session: Session,api_manager: ApiManager,create_credit_user_request: CreateCreditUserRequest,request_credit_invalid_request: RequestCreditRequest):
        api_manager.user_steps.request_credit_invalid(create_credit_user_request,request_credit_invalid_request)

        credit_from_db = Credit.get_credit_by_id(db_session, request_credit_invalid_request.accountId)
        assert credit_from_db is None, "Кредит получен, ошибка!"





