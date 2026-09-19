import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from src.main.api.models.create_credit_user_request import CreateCreditUserRequest
from src.main.api.models.repay_credit_request import RepayCreditRequest


@pytest.mark.api
class TestRepayCredit:
    def test_repay_credit(self,db_session: Session,api_manager: ApiManager,create_credit_user_request: CreateCreditUserRequest,repay_credit_request: RepayCreditRequest):
        response = api_manager.user_steps.repay_credit(create_credit_user_request,repay_credit_request)

        credit_from_db = Credit.get_credit_by_id(db_session, response.creditId)
        assert credit_from_db.id == response.creditId, "Кредит не погашен, id кредита нет в БД"

    def test_repay_credit_invalid(self,db_session: Session,api_manager: ApiManager,create_credit_user_request: CreateCreditUserRequest,repay_credit_invalid_request: RepayCreditRequest):
        api_manager.user_steps.repay_credit_invalid(create_credit_user_request, repay_credit_invalid_request)

        credit_from_db = Credit.get_credit_by_id(db_session, repay_credit_invalid_request.accountId)
        assert credit_from_db is None, "Кредит погашен, ошибка"

