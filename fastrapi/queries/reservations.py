from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool


class Error(BaseModel):
    message: str


class ReservationIn(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    phone_number: str
    party_size: str
    date: str
    time: str
    account_id: Optional[int]


class ReservationOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    party_size: str
    date: str
    time: str


class ReservationRepository:
    def create(
        self,
        reservations: ReservationIn
    ) -> Union[ReservationOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    if reservations.account_id is None:
                        reservations.account_id = None
                    else:
                        db.execute(
                            """
                            SELECT id FROM accounts WHERE id = %s
                            """,
                            [reservations.account_id]
                        )
                        existing_account = db.fetchone()
                        if existing_account is None:
                            return {"message": "Account not found."}

                    result = db.execute(
                        """
                        INSERT INTO reservations (
                            account_id
                            , first_name
                            , last_name
                            , phone_number
                            , email
                            , party_size
                            , date
                            , time
                            )
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id
                        , account_id
                        , first_name
                        , last_name
                        , phone_number
                        , email
                        , party_size
                        , date
                        , time;
                        """,
                        [
                            reservations.account_id,
                            reservations.first_name,
                            reservations.last_name,
                            reservations.phone_number,
                            reservations.email,
                            reservations.party_size,
                            reservations.date,
                            reservations.time
                        ]
                    )
                    record = result.fetchone()
                    return self.record_to_reservation_out(record)

        except Exception as e:
            print(e)
            return {"message": "Could not create reservation"}

    def get_all(self) -> Union[List[ReservationOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                            , account_id
                            , first_name
                            , last_name
                            , email
                            , phone_number
                            , party_size
                            , date
                            , time
                        FROM reservations
                        ORDER BY id
                        """
                    )
                    return [
                        self.record_to_reservation_out(record)
                        for record in result
                    ]

        except Exception as e:
            print(e)
            return {"message": "Could not get all reservations"}

    def get_one(
        self,
        reservation_id: int
    ) -> Union[ReservationOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id
                            , first_name
                            , last_name
                            , phone_number
                            , email
                            , party_size
                            , date
                            , time
                            , account_id
                        FROM reservations
                        WHERE id = %s
                        """,
                        [reservation_id]
                    )
                    record = db.fetchone()
                    if record is None:
                        return {"message": "Reservation not found"}

                    return self.record_to_reservation_out(record)

        except Exception as e:
            print(e)
            return {"message": "Could not get reservation"}

    def update(
        self,
        reservation_id: int,
        updated_reservation: ReservationIn
    ) -> Union[ReservationOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE reservations
                        SET first_name = %s,
                            last_name = %s,
                            phone_number = %s,
                            email = %s,
                            party_size = %s,
                            date = %s,
                            time = %s
                        WHERE id = %s
                        """,
                        [
                            updated_reservation.first_name,
                            updated_reservation.last_name,
                            updated_reservation.phone_number,
                            updated_reservation.email,
                            updated_reservation.party_size,
                            updated_reservation.date,
                            updated_reservation.time,
                            reservation_id,
                        ]
                    )

                    updated_reservation.id = reservation_id
                    return updated_reservation

        except Exception as e:
            print(e)
            return {"message": "Could not update reservation"}

    def delete(
        self,
        reservation_id: int
    ) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM reservations
                        WHERE id = %s
                        """,
                        [reservation_id]
                    )
                    return True

        except Exception as e:
            print(e)
            return False

    def reservation_in_to_out(self, id: int, reservations: ReservationIn):
        old_data = reservations.dict()
        return ReservationOut(id=id, **old_data)

    def record_to_reservation_out(self, record):
        return ReservationOut(
            id=record[0],
            first_name=record[1],
            last_name=record[2],
            phone_number=record[3],
            email=record[4],
            party_size=record[5],
            date=record[6],
            time=record[7],
            account_id=record[8],
        )
