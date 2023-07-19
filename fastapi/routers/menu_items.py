from fastapi import APIRouter, Depends
from typing import Union, List
from queries.menu_items import (
    MenuItemsIn,
    MenuItemsOut,
    MenuItemsRepository,
    Error,
)


router = APIRouter()


@router.post("/menu_items", response_model=Union[MenuItemsOut, Error])
def create_menu_item(
    menu_items: MenuItemsIn, repo: MenuItemsRepository = Depends()
):
    return repo.create(menu_items)


@router.get("/menu_items", response_model=Union[Error, List[MenuItemsOut]])
def list_menu_items(
    repo: MenuItemsRepository = Depends(),
):
    return repo.list_menu_items()


@router.put(
    "/menu_items/{menu_item_id}", response_model=Union[MenuItemsOut, Error]
)
def update_menu_item(
    menu_item_id: int,
    menu_items: MenuItemsIn,
    repo: MenuItemsRepository = Depends(),
) -> Union[Error, MenuItemsOut]:
    return repo.update(menu_item_id, menu_items)


@router.get(
    "/menu_items/{menu_item_id}", response_model=Union[MenuItemsOut, Error]
)
def get_menu_item(
    menu_item_id=int,
    repo: MenuItemsRepository = Depends(),
) -> bool:
    return repo.get_menu_item(menu_item_id)


@router.delete("/menu_items/{menu_item_id}", response_model=bool())
def delete_menu_item(
    menu_item_id: int,
    repo: MenuItemsRepository = Depends(),
) -> bool:
    return repo.delete(menu_item_id)
