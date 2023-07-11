from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool

class Error(BaseModel):
    message: str


class ReservationIn(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email_address: str
    party_size: str
    date: str
    time: str


class ReservationOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    email_address: str
    party_size: str
    date: str
    time: str


class ReservationRespoitory:
    def update(self, reservation_id: int, reservations: ReservationIn) -> Union[ReservationOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE reservations
                        SET first_name = %s
                            , last_name = %s
                            , phone_number = %s
                            , email_address = %s
                            , party_size = %s
                            , date = %s
                            , time = %s
                        WHERE id = %s
                        """,
                        [
                            reservations.first_name,
                            reservations.last_name,
                            reservations.phone_number,
                            reservations.email_address,
                            reservations.party_size,
                            reservations.date,
                            reservations.time,
                            reservation_id
                        ]
                    )
                    # old_data = accounts.dict()
                    # return AccountOut(id=account_id, **old_data)
                    return self.reservation_in_to_out(reservation_id, reservations)

        except Exception as e:
            print(e)
            return {"message": "Could not update reservation"}

    def get_all(self) -> Union[Error, List[ReservationOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, first_name, last_name, phone_number, email_address, party_size, date, time
                        FROM reservations
                        ORDER BY id
                        """
                    )
                    return [
                        ReservationOut(
                            id=entry[0],
                            first_name=entry[1],
                            last_name=entry[2],
                            phone_number=entry[3],
                            email_address=entry[4],
                            party_size=entry[5],
                            date=entry[6],
                            time=entry[7],
                        )
                        for entry in db
                    ]

        except Exception:
            return {"message": "Could not get all reservations"}

    def create(self, reservations: ReservationIn) -> ReservationOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO reservations
                            (first_name, last_name, phone_number, email_address, party_size, date, time)
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            reservations.first_name,
                            reservations.last_name,
                            reservations.phone_number,
                            reservations.email_address,
                            reservations.party_size,
                            reservations.date,
                            reservations.time
                        ]
                    )
                    id = result.fetchone()[0]
                    # old_data = accounts.dict()
                    # return AccountOut(id=id, **old_data)
                    # return {"message": "error!"}
                    return self.reservation_in_to_out(id, reservations)
        except Exception:
            return {"message": "Could not post new reservation"}

    def reservation_in_to_out(self, id: int, reservations: ReservationIn):
        old_data = reservations.dict()
        return ReservationOut(id=id, **old_data)
