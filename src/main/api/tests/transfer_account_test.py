import pytest
from src.main.api.classes.api_manager import ApiManager
from sqlalchemy.orm import Session
from src.main.api.db.crud.transfer_crud import TransferCrudDb as Transfer
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest


@pytest.mark.api
class TestTransferAccount:
    def test_transfer_account_valid(self,db_session: Session,api_manager: ApiManager,create_user_request: CreateUserRequest,transfer_account_request: TransferAccountRequest,deposit_account_request:DepositAccountRequest):
        api_manager.user_steps.deposit_account(create_user_request,deposit_account_request)
        response = api_manager.user_steps.transfer_account(create_user_request,transfer_account_request)

        transfer_from_db = Transfer.get_transfer_by_id(db_session, response.fromAccountId)
        assert transfer_from_db.from_account_id == response.fromAccountId, "Перевод не выполнен, не найден id отправителя"


    @pytest.mark.parametrize(
        "transfer_account_invalid_request",
        [499, 10001],
        indirect=True
    )

    def test_transfer_account_invalid(self,db_session: Session,api_manager: ApiManager,create_user_request: CreateUserRequest,transfer_account_invalid_request: TransferAccountRequest,deposit_account_transfer_request: DepositAccountRequest):
        api_manager.user_steps.deposit_account(create_user_request, deposit_account_transfer_request)
        api_manager.user_steps.transfer_account_invalid(create_user_request, transfer_account_invalid_request)

        transfer_from_db = Transfer.get_transfer_by_id(db_session, transfer_account_invalid_request.fromAccountId)
        assert transfer_from_db is None, "Перевод выполнен, ошибка"


