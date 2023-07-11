from fastapi import APIRouter, Depends
from typing import Union, List
from queries.menu import MenuIn, MenuOut, MenuRepository, Error


router = APIRouter()


@router.post("/menu", response_model=Union[MenuOut, Error])
def create_menu_item(menu: MenuIn, repo: MenuRepository = Depends()):
    return repo.create(menu)


@router.get("/menu", response_model=Union[Error, List[MenuOut]])
def list_menu(
    repo: MenuRepository = Depends(),
):
    return repo.list_menu()


@router.put("/menu/{menu_id}", response_model=Union[MenuOut, Error])
def update_menu_item(
    menu_id: int,
    menu_item: MenuIn,
    repo: MenuRepository = Depends(),
) -> Union[Error, MenuOut]:
    return repo.update(menu_id, menu_item)


@router.get("/menu/{menu_id}", response_model=Union[MenuOut, Error])
def get_menu_item(
    menu_id=int,
    repo: MenuRepository = Depends(),
) -> bool:
    return repo.get_menu_item(menu_id)


@router.delete("/menu/{menu_id}", response_model=bool())
def delete_menu_item(
    menu_id: int,
    repo: MenuRepository = Depends(),
) -> bool:
    return repo.delete(menu_id)
