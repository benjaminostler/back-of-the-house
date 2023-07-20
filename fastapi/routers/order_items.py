from fastapi import APIRouter, Depends
from typing import Union, List
from queries.order_items import (
    OrderItemsIn,
    OrderItemsOut,
    OrderItemsRepository,
    Error
)


router = APIRouter()


@router.put(
        "/order_items/{order_items_id}",
        response_model=Union[OrderItemsOut, Error],
        tags=["Order Items"],
        operation_id="update_order_items")
def update_order_items(
    order_items_id: int,
    order_items: OrderItemsIn,
    repo: OrderItemsRepository = Depends(),
) -> Union[OrderItemsOut, Error]:
    return repo.update(order_items_id, order_items)


@router.delete(
        "/order_items/{order_items_id}",
        response_model=bool,
        tags=["Order Items"],
        operation_id="delete_order_items")
def delete_order_items(
    order_items_id: int,
    repo: OrderItemsRepository = Depends(),
) -> bool:
    return repo.delete(order_items_id)


@router.post(
        "/order_items",
        response_model=Union[OrderItemsOut, Error],
        tags=["Order Items"],
        operation_id="create_order_items")
def create_order_items(
        order_items: OrderItemsIn,
        repo: OrderItemsRepository = Depends()):
    return repo.create(order_items)


@router.get(
        "/order_items",
        response_model=Union[Error, List[OrderItemsOut]],
        tags=["Order Items"],
        operation_id="list_order_items")
def list_order_items(
    repo: OrderItemsRepository = Depends(),
):
    return repo.get_all()
