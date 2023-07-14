from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.reservations import (
    Error,
    ReservationIn,
    ReservationRepository,
    ReservationOut,
)

router = APIRouter()


@router.post("/reservations", response_model=Union[ReservationOut, Error])
def create_reservations(
    reservations: ReservationIn,
    # response: Response,
    repo: ReservationRepository = Depends()
):
    # return repo.create(accounts)
    # response.status_code = 400
    return repo.create(reservations)
    # return accounts


@router.get("/reservations", response_model=Union[Error, List[ReservationOut]])
def get_all(
    repo: ReservationRepository = Depends(),
):
    return repo.get_all()

@router.put("/reservations/{reservation_id}", response_model=Union[ReservationOut, Error])
def update_reservation(
    reservation_id: int,
    reservation: ReservationIn,
    repo: ReservationRepository = Depends(),
) -> Union[Error, ReservationOut]:
    return repo.update(reservation_id, reservation)

@router.delete("/reservations/{reservation_id}", response_model=bool)
def delete_reservation(
    reservation_id: int,
    repo: ReservationRepository = Depends(),
) -> bool:
    return repo.delete(reservation_id)


@router.get("/reservations/{reservation_id}", response_model=Optional[ReservationOut])
def get_one_reservation(
    reservation_id: int,
    response: Response,
    repo: ReservationRepository = Depends(),
) -> ReservationOut:
    reservation = repo.get_one(reservation_id)
    if reservation is None:
        response.status_code = 404
    return reservation
