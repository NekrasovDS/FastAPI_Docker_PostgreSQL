from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/accounts/", response_model=_schemas.Accounts)
async def create_accounts(
        accounts: _schemas.CreateAccounts,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_accounts(accounts=accounts, db=db)


@app.get("/api/accounts/", response_model=List[_schemas.Accounts])
async def get_accounts(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_accounts(db=db)


@app.get("/api/accounts/{account_id}/", response_model=_schemas.Accounts)
async def get_account(
    account_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    accounts = await _services.get_accounts(db=db, account_id=account_id)
    if accounts is None:
        raise _fastapi.HTTPException(status_code=404, detail="Account does not exist")

    return accounts


@app.delete("/api/accounts/{account_id}/")
async def delete_account(
    account_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    accounts = await _services.get_accounts(db=db, account_id=account_id)
    if accounts is None:
        raise _fastapi.HTTPException(status_code=404, detail="Account does not exist")

    await _services.delete_accounts(accounts, db=db)

    return "successfully deleted the user"


@app.put("/api/accounts/{account_id}/", response_model=_schemas.Accounts)
async def update_account(
    account_id: int,
    accounts_data: _schemas.CreateAccounts,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    accounts = await _services.get_accounts(db=db, account_id=account_id)
    if accounts is None:
        raise _fastapi.HTTPException(status_code=404, detail="Account does not exist")

    return await _services.update_accounts(
        accounts_data=accounts_data, accounts=accounts, db=db
    )
