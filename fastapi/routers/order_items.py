from fastapi import APIRouter, Depends
from typing import Union, List
from queries.order_items import (OrderItemsIn, OrderItemsOut, OrderItemsRepository, Error)


router = APIRouter()


@router.post("/order_items", response_model=Union[OrderItemsOut, Error])
def create_order_items(order_items: OrderItemsIn, repo: OrderItemsRepository = Depends()):
    return repo.create(order_items)


@router.get("/order_items/{order_items_id}", response_model=Union[Error, OrderItemsOut])
def get_order_items(
        order_items_id: int,
        repo: OrderItemsRepository = Depends(),
) -> OrderItemsOut:
    return repo.get_order_items(order_items_id)


@router.get("/order_items", response_model=Union[Error, List[OrderItemsOut]])
def list_order_items(
    repo: OrderItemsRepository = Depends(),
):
    return repo.list_order_items()


@router.put("/order_items/{order_items_id}", response_model=Union[OrderItemsOut, Error])
def update_order_items(
    order_items_id: int,
    order_items: OrderItemsIn,
    repo: OrderItemsRepository = Depends(),
) -> Union[OrderItemsOut, Error]:
    return repo.update(order_items_id, order_items)


@router.delete("/order_items/{order_items_id}", response_model=Union[OrderItemsOut, Error])
def delete_order_items(
    order_items_id: int,
    repo: OrderItemsRepository = Depends(),
) -> bool:
    return repo.delete(order_items_id)