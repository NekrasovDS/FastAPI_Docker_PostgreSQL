from typing import TYPE_CHECKING

import database as _database
import models as _models
import schemas as _schemas

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


async def create_account(accounts: _schemas.CreateAccount, db: "Session") -> _schemas.Accounts:
    accounts = _models.Accounts(**accounts.dict())
    db.add(accounts)
    db.commit()
    db.refresh(accounts)
    return _schemas.Accounts.from_orm(accounts)
