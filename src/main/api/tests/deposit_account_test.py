import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb as Account
from sqlalchemy.orm import Session
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest


@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account_valid(self,db_session: Session, api_manager: ApiManager,create_user_request: CreateUserRequest,deposit_account_request: DepositAccountRequest):
        response = api_manager.user_steps.deposit_account(create_user_request,deposit_account_request)
        assert response.balance == 2000

        account_from_db = Account.get_account_by_id(db_session, response.id)
        assert account_from_db.id == response.id, "Аккаунт не создан, id аккаунта нет в БД"
        assert account_from_db.balance == 2000, "Баланс не пополнен"

    def test_deposit_account_invalid(self,db_session: Session, api_manager: ApiManager,create_user_request: CreateUserRequest,deposit_account_invalid_request: DepositAccountRequest):
        api_manager.user_steps.deposit_account_invalid(create_user_request,deposit_account_invalid_request)

        account_from_db = Account.get_account_by_id(db_session, deposit_account_invalid_request.accountId)
        assert account_from_db.balance == 0, "Баланс пополнен на невалидную сумму, ошибка"
