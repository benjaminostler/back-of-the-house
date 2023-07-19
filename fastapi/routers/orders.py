from fastapi import APIRouter, Depends
from typing import Union, List
from queries.orders import (OrderIn, OrderOut, OrderRepository, Error)


router = APIRouter()


@router.post(
        "/order",
        response_model=Union[OrderOut, Error],
        tags=["Orders"],
        operation_id="create_order")
def create_order(
        orders: OrderIn,
        repo: OrderRepository = Depends()):
    return repo.create(orders)


@router.get("/order/{orders_id}",
            response_model=Union[Error, OrderOut],
            tags=["Orders"],
            operation_id="get_order_by_id")
def get_detail_order(
        orders_id: int,
        repo: OrderRepository = Depends(),
) -> OrderOut:
    return repo.get_order(orders_id)


@router.get("/order",
            response_model=Union[Error, List[OrderOut]],
            tags=["Orders"],
            operation_id="get_orders_by_id")
def list_orders(
    repo: OrderRepository = Depends(),
):
    return repo.get_orders()



@router.put("/order/{orders_id}",
            response_model=Union[OrderOut, Error],
            tags=["Orders"],
            operation_id="update_order_by_id")
def update_order(
    orders_id: int,
    orders: OrderIn,
    repo: OrderRepository = Depends(),
) -> Union[OrderOut, Error]:
    return repo.update(orders_id, orders)


@router.delete("/order/{orders_id}",
               response_model=Union[OrderOut, Error],
               tags=["Orders"],
               operation_id="delete_order_by_id")
def delete_order(
    orders_id: int,
    repo: OrderRepository = Depends(),
) -> bool:
    return repo.delete(orders_id)
