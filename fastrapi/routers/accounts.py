from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel
from typing import Union, List
from queries.accounts import (
    Error,
    AccountIn,
    AccountOut,
    AccountRepository,
    DuplicateAccountError,
    AccountUpdate,
)
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: AccountOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post(
        "/api/accounts",
        tags=["Accounts"],
        response_model=AccountToken | HttpError,
)
async def create_account(
    info: AccountIn,
    request: Request,
    response: Response,
    repo: AccountRepository = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = AccountOut(**repo.create(info, hashed_password).dict())
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())


@router.get(
    "/accounts/",
    tags=["Accounts"],
    response_model=Union[List[AccountOut], Error]
)
async def get_all_accounts(
    response: Response,
    repo: AccountRepository = Depends(),
    account: dict = Depends(authenticator.try_get_current_account_data),
) -> Union[AccountOut, Error]:
    if account is None:
        response.status_code = 401
        return Error(message="Sign in to get a specific account.")
    result = repo.get_all()
    if result is None:
        response.status_code = 404
        result = Error(message="No accounts exist.")
    return result


@router.put(
    "/accounts/{account_id}/",
    tags=["Accounts"],
    response_model=Union[AccountOut, Error],
)
async def update_one_account(
    id: int,
    account_update: AccountUpdate,
    response: Response,
    repo: AccountRepository = Depends(),
    account: dict = Depends(authenticator.try_get_current_account_data),
) -> Union[Error, AccountOut]:
    if account is None:
        response.status_code = 401
        return Error(message="Sign in to update a user.")
    return repo.update(id, account_update)


@router.delete(
    "/accounts/{account_id}",
    tags=["Accounts"],
    response_model=bool
)
async def delete_user(
    id: int,
    repo: AccountRepository = Depends(),
) -> bool:
    return repo.delete(id)


@router.get(
    "/token",
    tags=["Authentication"],
    response_model=AccountToken | None
)
async def get_token(
    request: Request,
    account: AccountOut = Depends(authenticator.try_get_current_account_data),
):
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }
