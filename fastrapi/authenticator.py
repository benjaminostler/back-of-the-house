import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.accounts import (
    AccountRepository,
    AccountOut,
    AccountOutWithPassword
)


class OurAuthenticator(Authenticator):
    async def get_account_data(
        self,
        username: str,
        accounts: AccountRepository,
    ):
        return accounts.get(username)

    def get_account_getter(
        self,
        accounts: AccountRepository = Depends(),
    ):
        return accounts

    def get_hashed_password(self, account: AccountOutWithPassword):
        return account.hashed_password

    def get_account_data_for_cookie(self, account: AccountOutWithPassword):
        return account.username, AccountOut(**account.dict())


authenticator = OurAuthenticator(os.environ["SIGNING_KEY"])
