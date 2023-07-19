from fastapi import APIRouter, Depends
from typing import Union, List
from queries.menu_items import (
    MenuItemsIn,
    MenuItemsOut,
    MenuItemsRepository,
    Error,
)


router = APIRouter()


@router.post("/menu_item", response_model=Union[MenuItemOut, Error], tags=["Menu Items"])
def create_menu_item(
    menu_items: MenuItemsIn, repo: MenuItemsRepository = Depends()
):
    return repo.create(menu_items)


@router.get("/menu_item", response_model=Union[Error, List[MenuItemOut]], tags=["Menu Items"])
def list_menu_items(
    repo: MenuItemsRepository = Depends(),
):
    return repo.list_menu_items()


@router.put(
    "/menu_item/{menu_item_id}", response_model=Union[MenuItemOut, Error], tags=["Menu Items"]
)
def update_menu_item(
    menu_item_id: int,
    menu_items: MenuItemsIn,
    repo: MenuItemsRepository = Depends(),
) -> Union[Error, MenuItemsOut]:
    return repo.update(menu_item_id, menu_items)


@router.get(
    "/menu_item/{menu_item_id}", response_model=Union[MenuItemOut, Error], tags=["Menu Items"]
)
def get_menu_item(
    menu_item_id=int,
    repo: MenuItemsRepository = Depends(),
) -> bool:
    return repo.get_menu_item(menu_item_id)


@router.delete("/menu_item/{menu_item_id}", response_model=bool(), tags=["Menu Items"])
def delete_menu_item(
    menu_item_id: int,
    repo: MenuItemsRepository = Depends(),
) -> bool:
    return repo.delete(menu_item_id)
