from fastapi import APIRouter, Depends
from typing import Union, List
from queries.order_items import (OrderItemsIn, OrderItemsOut, OrderItemsRepository, Error)


router = APIRouter()


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
