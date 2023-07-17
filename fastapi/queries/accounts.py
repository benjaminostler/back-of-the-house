from pydantic import BaseModel
from typing import List, Union
from queries.pool import pool


class Error(BaseModel):
    message: str

class DuplicateAccountError(ValueError):
    pass

class DuplicateAccountError(ValueError):
    pass


class DuplicateAccountError(ValueError):
    pass


class AccountIn(BaseModel):
    first_name: str
    last_name: str
    username: str
    hashed_password: str
    email: str
    phone_number: str


class AccountOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    phone_number: str


class AccountOutWithPassword(AccountOut):
    hashed_password: str


class AccountRepository:
    def get(self, username: str) -> AccountOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                            , first_name
                            , last_name
                            , username
                            , hashed_password
                            , email
                            , phone_number
                        FROM accounts
                        WHERE username =%s
                        """,
                        [username],
                    )
                    record = result.fetchone()
                    return self.record_to_account(record)
        except Exception as e:
            print(e)
            raise ValueError("Could not get account") from e

    def update(self, id: int, hashed_password: str, accounts: AccountIn) -> Union[AccountOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE accounts
                        SET first_name = %s
                            , last_name = %s
                            , username = %s
                            , hashed_password = %s
                            , email = %s
                            , phone_number = %s
                        WHERE id = %s
                        """,
                        [
                            accounts.first_name,
                            accounts.last_name,
                            accounts.username,
                            accounts.hashed_password,
                            accounts.email,
                            accounts.phone_number,
                            id,
                        ]
                    )
                    return AccountOut(
                        id=id,
                        first_name=accounts.first_name,
                        last_name=accounts.last_name,
                        username=accounts.username,
                        email=accounts.email,
                        phone_number=accounts.phone_number
                    )
        except Exception as e:
            print(e)
            return {"message": "Could not update account"}

    def get_all(self) -> Union[Error, List[AccountOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT * FROM accounts
                        WHERE username =%s
                        """,
                        [username],
                    )
                    record = result.fetchone()
                    return self.record_to_account(record)
        except Exception as e:
            print(e)
            raise ValueError("Could not get account") from e

    def update(self, id: int, hashed_password: str, accounts: AccountIn) -> Union[AccountOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE accounts
                        SET first_name = %s
                            , last_name = %s
                            , username = %s
                            , password = %s
                            , email = %s
                            , phone_number = %s
                        WHERE id = %s
                        """,
                        [
                            accounts.first_name,
                            accounts.last_name,
                            accounts.username,
                            hashed_password,
                            accounts.email,
                            accounts.phone_number,
                            id,
                        ]
                    )
                    return AccountOut(
                        id=id,
                        first_name=accounts.first_name,
                        last_name=accounts.last_name,
                        username=accounts.username,
                        email=accounts.email,
                        phone_number=accounts.phone_number
                    )
        except Exception as e:
            print(e)
            return {"message": "Could not update account"}

    def get_all(self) -> Union[Error, List[AccountOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT * FROM accounts
                        ORDER BY id
                        """
                    )
                    return [
                        AccountOut(
                            id=entry[0],
                            first_name=entry[1],
                            last_name=entry[2],
                            username=entry[3],
                            hashed_password=entry[4],
                            email=entry[5],
                            phone_number=entry[6],
                        )
                        for entry in db
                    ]
        except Exception:
            return {"message": "Could not get all accounts"}

    def create(self, info: AccountIn, hashed_password: str) -> AccountOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO accounts
                        (first_name, last_name, username, hashed_password, email, phone_number)
                    VALUES
                        (%s, %s, %s, %s, %s, %s)
                    RETURNING id, email, hashed_password;
                    """,
                    [
                        info.first_name,
                        info.last_name,
                        info.username,
                        hashed_password,
                        info.email,
                        info.phone_number
                    ]
                )
                id = result.fetchone()[0]
                return AccountOutWithPassword(
                    id=id,
                    first_name=info.first_name,
                    last_name=info.last_name,
                    username=info.username,
                    hashed_password=hashed_password,
                    email=info.email,
                    phone_number=info.phone_number
                )

    def record_to_account(self, record) -> AccountOutWithPassword:
        return AccountOutWithPassword(
            id=record[0],
            first_name=record[1],
            last_name=record[2],
            username=record[3],
            hashed_password=record[4],
            email=record[5],
            phone_number=record[6],
        )
        # account_dict = {
        #     "id": record[0],
        #     "first_name": record[1],
        #     "last_name": record[2],
        #     "username": record[3],
        #     "hashed_password": record[4],
        #     "email": record[5],
        #     "phone_number": record[6]
        # }
        # return account_dict

    def account_in_to_out(self, id: int, accounts: AccountIn):
        old_data = accounts.dict()
        return AccountOut(id=id, **old_data)
    def create(self, info: AccountIn, hashed_password: str) -> AccountOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO accounts
                        (first_name, last_name, username, hashed_password, email, phone_number)
                    VALUES
                        (%s, %s, %s, %s, %s, %s)
                    RETURNING id, email, hashed_password;
                    """,
                    [
                        info.first_name,
                        info.last_name,
                        info.username,
                        hashed_password,
                        info.email,
                        info.phone_number
                    ]
                )
                id = result.fetchone()[0]
                return AccountOutWithPassword(
                    id=id,
                    first_name=info.first_name,
                    last_name=info.last_name,
                    username=info.username,
                    hashed_password=hashed_password,
                    email=info.email,
                    phone_number=info.phone_number
                )

    def record_to_account(self, record) -> AccountOutWithPassword:
        return AccountOutWithPassword(
            id=record[0],
            first_name=record[1],
            last_name=record[2],
            username=record[3],
            hashed_password=record[4],
            email=record[5],
            phone_number=record[6],
        )
        # account_dict = {
        #     "id": record[0],
        #     "first_name": record[1],
        #     "last_name": record[2],
        #     "username": record[3],
        #     "hashed_password": record[4],
        #     "email": record[5],
        #     "phone_number": record[6]
        # }
        # return account_dict

    def account_in_to_out(self, id: int, accounts: AccountIn):
        old_data = accounts.dict()
        return AccountOut(id=id, **old_data)
