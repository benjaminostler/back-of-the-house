from pydantic import BaseModel
from fastapi import HTTPException
from queries.pool import pool


class Error(BaseModel):
    message: str


class DuplicateAccountError(ValueError):
    pass


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
    hashed_password: str
    email: str
    phone_number: str


class AccountRepository:
    def create(self, info: AccountIn, hashed_password: str) -> AccountOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                            INSERT INTO accounts (
                                first_name
                                , last_name
                                , username
                                , hashed_password
                                , email
                                , phone_number)
                            VALUES
                                (%s, %s, %s, %s, %s, %s)
                            RETURNING id
                            , first_name
                            , last_name
                            , username
                            , hashed_password
                            , email
                            , phone_number
                            """,
                        [
                            info.first_name,
                            info.last_name,
                            info.username,
                            hashed_password,
                            info.email,
                            info.phone_number,
                        ],
                    )
                    id = result.fetchone()[0]
                    return AccountOut(
                        id=id,
                        first_name=info.first_name,
                        last_name=info.last_name,
                        username=info.username,
                        hashed_password=hashed_password,
                        email=info.email,
                        phone_number=info.phone_number,
                    )
        except Exception:
            return {"message": "Could not create user"}

    def get_all(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT * FROM accounts
                    """
                )
                record = db.fetchall()
                return self.record_to_all_account_out(record)

    def get_one(self, username: str):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT * FROM accounts
                    WHERE username = %s
                    """,
                    [username],
                )
                record = db.fetchone()
                return self.record_to_account_out(record)

    def update(self, account_id, account_update):
        with pool.connection() as conn:
            with conn.cursor() as db:
                returned_values = None
                if account_update.first_name:
                    result = db.execute(
                        """
                        UPDATE accounts
                        SET first_name = %s
                        WHERE id = %s
                        RETURNING *
                        """,
                        [account_update.first_name, account_id],
                    )
                if account_update.last_name:
                    result = db.execute(
                        """
                        UPDATE accounts
                        SET last_name = %s
                        WHERE id = %s
                        RETURNING *
                        """,
                        [account_update.last_name, account_id],
                    )
                if account_update.username:
                    result = db.execute(
                        """
                        UPDATE accounts
                        SET username = %s
                        WHERE id = %s
                        RETURNING *
                        """,
                        [account_update.username, account_id]
                    )
                if account_update.email:
                    result = db.execute(
                        """
                        UPDATE accounts
                        SET email = %s
                        WHERE id = %s
                        RETURNING *
                        """,
                        [account_update.email, account_id],
                    )
                if account_update.phone_number:
                    result = db.execute(
                        """
                        UPDATE accounts
                        SET phone_number = %s
                        WHERE id = %s
                        RETURNING *
                        """,
                        [account_update.phone_number, account_id],
                    )
                returned_values = result.fetchone()
                return self.record_to_account(returned_values)

    def delete(self, account_id: int) -> None:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM accounts
                        WHERE id = %s
                        """,
                        [account_id]
                    )
                    if db.rowcount == 0:
                        raise HTTPException(
                            status_code=404,
                            detail=f"ID {account_id} does not exist",
                        )
            conn.commit()
            raise HTTPException(
                status_code=200,
                detail=f"accountID:{account_id} has been deleted",
            )
        except HTTPException as e:
            raise e

    def record_to_account(self, record):
        if record is None:
            return None
        return AccountOut(
            id=record[0],
            first_name=record[1],
            last_name=record[2],
            username=record[3],
            hashed_password=record[4],
            email=record[5],
            phone_number=record[6],
        )

    def record_to_account_out(self, record):
        return AccountOut(
            id=record[0],
            first_name=record[1],
            last_name=record[2],
            username=record[3],
            hashed_password=record[4],
            email=record[5],
            phone_number=record[6],
        )

    def record_to_all_account_out(self, records):
        accounts = []
        for record in records:
            accounts.append(
                AccountOut(
                    id=record[0],
                    first_name=record[1],
                    last_name=record[2],
                    username=record[3],
                    hashed_password=record[4],
                    email=record[5],
                    phone_number=record[6],
                )
            )
        return accounts
