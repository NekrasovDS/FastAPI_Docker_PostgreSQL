from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas
from fastapi import FastAPI, File, Form, UploadFile

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

import sys
print(sys.getdefaultencoding())


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_accounts(accounts: _schemas.CreateAccounts, db: "Session") -> _schemas.Accounts:
    accounts = _models.Accounts(**accounts.dict())
    db.add(accounts)
    db.commit()
    db.refresh(accounts)
    return _schemas.Accounts.from_orm(accounts)


async def get_all_accounts(db: "Session") -> List[_schemas.Accounts]:
    accounts = db.query(_models.Accounts).all()
    return list(map(_schemas.Accounts.from_orm, accounts))


async def get_accounts(account_id: int, db: "Session"):
    accounts = db.query(_models.Accounts).filter(_models.Accounts.id == account_id).first()
    return accounts


async def delete_accounts(accounts: _models.Accounts, db: "Session"):
    db.delete(accounts)
    db.commit()


async def update_accounts(
    accounts_data: _schemas.CreateAccounts, accounts: _models.Accounts, db: "Session"
) -> _schemas.Accounts:
    accounts.first_name = accounts_data.TIN
    accounts.last_name = accounts_data.CRR
    accounts.email = accounts_data.legal_name
    accounts.phone_number = accounts_data.registration_date

    db.commit()
    db.refresh(accounts)

    return _schemas.Accounts.from_orm(accounts)
