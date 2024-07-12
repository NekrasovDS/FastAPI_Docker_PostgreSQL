import datetime as _dt
import pydantic as _pydantic


class _BaseAccounts(_pydantic.BaseModel):
    TIN: int
    CRR: int
    legal_name: str


class Accounts(_BaseAccounts):
    id: int
    registration_date: _dt.datetime

    
class CreateAccount(_BaseAccounts):
    pass
