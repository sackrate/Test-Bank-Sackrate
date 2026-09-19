from sqlalchemy.orm import Session
from src.main.api.db.models.transaction_table import Transaction


class TransferCrudDb:
    @staticmethod
    def get_transfer_by_id(db: Session, transfer_id: int) -> Transaction | None:
        return db.query(Transaction).filter_by(from_account_id=transfer_id).first()
