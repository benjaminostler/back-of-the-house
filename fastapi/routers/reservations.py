from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.reservations import (
    Error,
    ReservationIn,
    ReservationRespoitory,
    ReservationOut,
)

router = APIRouter()


@router.post("/reservations", response_model=Union[ReservationOut, Error])
def create_reservations(
    reservations: ReservationIn,
    # response: Response,
    repo: ReservationRespoitory = Depends()
):
    # return repo.create(accounts)
    # response.status_code = 400
    return repo.create(reservations)
    # return accounts


@router.get("/reservations", response_model=Union[Error, List[ReservationOut]])
def get_all(
    repo: ReservationRespoitory = Depends(),
):
    return repo.get_all()

@router.put("/reservations/{reservation_id}", response_model=Union[ReservationOut, Error])
def update_reservation(
    reservation_id: int,
    reservation: ReservationIn,
    repo: ReservationRespoitory = Depends(),
) -> Union[Error, ReservationOut]:
    return repo.update(reservation_id, reservation)
