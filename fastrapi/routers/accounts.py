from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel
from typing import Union, List, Optional
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

router = APIRouter()


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: AccountOut


class HttpError(BaseModel):
    detail: str


@router.post(
        "/api/accounts/",
        response_model=AccountToken | HttpError,
        tags=["Accounts"]
)
async def create(
    info: AccountIn,
    request: Request,
    response: Response,
    repo: AccountRepository = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = repo.create(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account with those credentials already exists."
        )
    form = AccountForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())


@router.get(
        "/accounts/",
        response_model=Union[Error, List[AccountOut]],
        tags=["Accounts"]
)
def get_all(
    repo: AccountRepository = Depends(),
):
    return repo.get_all()


@router.get(
        "/accounts/{username}",
        response_model=Optional[AccountOut],
        tags=["Accounts"]
)
def get_one(
    username: str,
    response: Response,
    repo: AccountRepository = Depends(),
) -> AccountOut:
    user = repo.get_one(username)
    if user is None:
        response.status_code = 404
    return user


@router.patch(
        "/accounts/{username}",
        response_model=AccountOut,
        tags=["Accounts"]
)
def update(
    username: str,
    info: AccountUpdate,
    response: Response,
    queries: AccountRepository = Depends(),
):
    record = queries.update(username, info)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.delete(
        "/accounts/{account_id}",
        response_model=bool,
        tags=["Accounts"]
)
def delete_job(
    account_id: int,
    repo: AccountRepository = Depends(),
) -> bool:
    return repo.delete(account_id)


@router.get(
        "/token",
        response_model=AccountToken | None,
        tags=["Auth"]
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
