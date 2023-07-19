from fastapi import APIRouter, Depends
from typing import Union, List
from queries.orders import (OrderIn, OrderOut, OrderRepository, Error)


router = APIRouter()


@router.get("/order",
            response_model=Union[Error, List[OrderOut]],
            tags=["Orders"],
            operation_id="get_orders_by_id")
def list_orders(
    repo: OrderRepository = Depends(),
):
    return repo.get_orders()
