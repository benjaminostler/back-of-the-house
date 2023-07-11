from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.accounts import (
    Error,
    AccountIn,
    AccountRespoitory,
    AccountOut,
)

router = APIRouter()


@router.post("/accounts", response_model=Union[AccountOut, Error])
def create_accounts(
    accounts: AccountIn,
    # response: Response,
    repo: AccountRespoitory = Depends()
):
    # return repo.create(accounts)
    # response.status_code = 400
    return repo.create(accounts)
    # return accounts


@router.get("/accounts", response_model=Union[Error, List[AccountOut]])
def get_all(
    repo: AccountRespoitory = Depends(),
):
    return repo.get_all()

@router.put("/accounts/{account_id}", response_model=Union[AccountOut, Error])
def update_account(
    account_id: int,
    account: AccountIn,
    repo: AccountRespoitory = Depends(),
) -> Union[Error, AccountOut]:
    return repo.update(account_id, account)
