from fastapi import APIRouter, Depends
from typing import Union, List
from queries.cart_items import (
    CartItemIn,
    CartItemOut,
    Error,
    CartItemRepository,
)


router = APIRouter()


@router.post(
    "/cart_item",
    response_model=Union[CartItemOut, Error],
    tags=["Cart Items"],
    operation_id="create_cart_item",
)
def create_cart_item(
    cart_item: CartItemIn, repo: CartItemRepository = Depends()
):
    return repo.create(cart_item)


@router.get(
    "/cart_items",
    response_model=Union[Error, List[CartItemOut]],
    tags=["Cart Items"],
    operation_id="list_cart_items",
)
def list_cart_items(
    repo: CartItemRepository = Depends(),
):
    return repo.list()


@router.get(
    "/cart_item/{cart_item_id}",
    response_model=Union[CartItemOut, Error],
    tags=["Cart Items"],
    operation_id="get_cart_item",
)
def get_cart_item(
    cart_item_id: int, repo: CartItemRepository = Depends()
) -> Union[Error, CartItemOut]:
    return repo.get(cart_item_id)


@router.put(
    "/cart_item/{cart_item_id}",
    response_model=Union[CartItemOut, Error],
    tags=["Cart Items"],
    operation_id="update_cart_item",
)
def update_cart_item(
    cart_item_id: int,
    cart_item: CartItemIn,
    repo: CartItemRepository = Depends(),
) -> Union[Error, CartItemOut]:
    return repo.update(cart_item_id, cart_item)


@router.delete(
    "/cart_item/{cart_item_id}",
    response_model=Union[CartItemOut, Error],
    tags=["Cart Items"],
    operation_id="delete_cart_item",
)
def delete_cart_item(
    cart_item_id: int, repo: CartItemRepository = Depends()
) -> Union[Error, str]:
    return repo.delete(cart_item_id)
