from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/accounts/", response_model=_schemas.Accounts)
async def create_account(
        accounts: _schemas.CreateAccount,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_account(accounts=accounts, db=db)

