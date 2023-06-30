from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool

class Error(BaseModel):
    message: str


class AccountIn(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str
    phone_number: str


class AccountOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    password: str
    email: str
    phone_number: str


class AccountRespoitory:
    def get_all(self) -> Union[Error, List[AccountOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, first_name, last_name, username, password, email, phone_number
                        FROM accounts
                        ORDER BY id
                        """
                    )
                    return [
                        AccountOut(
                            id=entry[0],
                            first_name=entry[1],
                            last_name=entry[2],
                            username=entry[3],
                            password=entry[4],
                            email=entry[5],
                            phone_number=entry[6],
                        )
                        for entry in db
                    ]

        except Exception:
            return {"message": "Could not get all accounts"}

    def create(self, accounts: AccountIn) -> AccountOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO accounts
                            (first_name, last_name, username, password, email, phone_number)
                        VALUES
                            (%s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            accounts.first_name,
                            accounts.last_name,
                            accounts.username,
                            accounts.password,
                            accounts.email,
                            accounts.phone_number
                        ]
                    )
                    id = result.fetchone()[0]
                    old_data = accounts.dict()
                    return AccountOut(id=id, **old_data)
                    # return {"message": "error!"}
        except Exception:
            return {"message": "Could not post new account"}
