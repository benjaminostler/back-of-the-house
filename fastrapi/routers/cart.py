from fastapi import APIRouter, Depends
from typing import Union
from queries.cart import (
    CartRepository,
    CartOut,
    Error,
)


router = APIRouter()


@router.post(
    "/cart",
    response_model=Union[CartOut, Error],
    tags=["Cart"],
    operation_id="create_cart",
)
def create_cart(repo: CartRepository = Depends()):
    return repo.create()


@router.get(
    "/cart/{cart_id}",
    response_model=Union[Error, CartOut],
    tags=["Cart"],
    operation_id="get_cart_by_id",
)
def get_cart_detail(cart_id: int, repo: CartRepository = Depends()) -> CartOut:
    return repo.get_cart(cart_id)


@router.delete(
    "/cart/{cart_id}",
    response_model=Union[Error, bool],
    tags=["Cart"],
    operation_id="delete_cart_by_id",
)
def delete_cart(cart_id: int, repo: CartRepository = Depends()) -> bool:
    return repo.delete(cart_id)
