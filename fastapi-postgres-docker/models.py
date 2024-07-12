import datetime as _dt
import sqlalchemy as _sql
from sqlalchemy import CheckConstraint


import database as _database


class Accounts(_database.Base):
    __tablename__ = "accounts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    TIN = _sql.Column(_sql.Integer, index=True)
    CRR = _sql.Column(_sql.Integer, index=True)
    legal_name = _sql.Column(_sql.Text, index=True)
    registration_date = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow, index=True)


class Agreements (_database.Base):
    __tablename__ = "agreements"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    start_date = _sql.Column(_sql.Date)
    end_date = _sql.Column(_sql.Date)
    agreement_id = _sql.Column(_sql.Integer, _sql.ForeignKey("agreements.id"), nullable=True)
    account_id = _sql.Column(_sql.Integer, _sql.ForeignKey(Accounts.id))


__table_args__ = (
        CheckConstraint("agreement_id != id", name="agreement_id_not_equal_id"),
    )
