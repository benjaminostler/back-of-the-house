from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool

class Error(BaseModel):
    message: str


class ReservationIn(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    party_size: str
    date: str
    time: str


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
    def get_one(self, reservation_id: int) -> Optional[ReservationOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                            , first_name
                            , last_name
                            , email
                            , phone_number
                            , party_size
                            , date
                            , time
                        FROM reservations
                        WHERE id = %s
                        """,
                        [reservation_id]
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_reservation_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that reservation"}

    def delete(self, reservation_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE from reservations
                        WHERE id = %s
                        """,
                        [reservation_id]
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(self, reservation_id: int, reservations: ReservationIn) -> Union[ReservationOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE reservations
                        SET first_name = %s
                            , last_name = %s
                            , email = %s
                            , phone_number = %s
                            , party_size = %s
                            , date = %s
                            , time = %s
                        WHERE id = %s
                        """,
                        [
                            reservations.first_name,
                            reservations.last_name,
                            reservations.email,
                            reservations.phone_number,
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
                        SELECT id
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

        except Exception:
            return {"message": "Could not get all reservations"}

    def create(self, reservations: ReservationIn) -> ReservationOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO reservations
                            (first_name, last_name, email, phone_number, party_size, date, time)
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            reservations.first_name,
                            reservations.last_name,
                            reservations.email,
                            reservations.phone_number,
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

    def record_to_reservation_out(self, record):
        return ReservationOut(
            id=record[0],
            first_name=record[1],
            last_name=record[2],
            email=record[3],
            phone_number=record[4],
            party_size=record[5],
            date=record[6],
            time=record[7],
        )
