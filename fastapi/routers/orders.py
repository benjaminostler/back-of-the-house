from fastapi import APIRouter, Depends
from typing import Union, List
from queries.orders import (OrderIn, OrderOut, OrderRepository, Error)


router = APIRouter()


@router.post("/order", response_model=Union[OrderOut, Error])
def create_order(order: OrderIn, repo: OrderRepository = Depends()):
    return repo.create(order)


@router.get("/order/{order_id}", response_model=Union[Error, OrderOut])
def get_detail_order(
        order_id: int,
        repo: OrderRepository = Depends(),
) -> OrderOut:
    return repo.get_order(order_id)


@router.get("/orders", response_model=Union[Error, List[OrderOut]])
def list_orders(
    repo: OrderRepository = Depends(),
):
    return repo.list_orders()


@router.put("/order/{order_id}", response_model=Union[OrderOut, Error])
def update_order(
    order_id: int,
    order: OrderIn,
    repo: OrderRepository = Depends(),
) -> Union[OrderOut, Error]:
    return repo.update(order_id, order)


@router.delete("/order/{order_id}", response_model=Union[OrderOut, Error])
def delete_order(
    order_id: int,
    repo: OrderRepository = Depends(),
) -> bool:
    return repo.delete(order_id)
