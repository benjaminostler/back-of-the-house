from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool


class Error(BaseModel):
    message: str


class MenuItemIn(BaseModel):
    category: str
    name: str
    picture_url: Optional[str]
    description: str
    price: float


class MenuItemOut(BaseModel):
    id: int
    category: str
    name: str
    picture_url: Optional[str]
    description: str
    price: float


class MenuItemRepository:
    def get_menu_item(self, menu_item_id: int) -> Optional[MenuItemOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, category, name, picture_url, description, price
                        FROM menu_items
                        WHERE id = %s
                        """,
                        [menu_item_id],
                    )
                    record = result.fetchone()
                    return self.record_to_menu_item_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not retrieve item info."}

    def delete(self, menu_item_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM menu_items
                        WHERE id = %s
                        """,
                        [menu_item_id],
                    )
            return True
        except Exception as e:
            print(e)
            return False

    def update(
        self, menu_item_id: int, menu_item: MenuItemIn
    ) -> Union[Error, List[MenuItemOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE menu_items
                        SET category = %s,
                        name = %s,
                        picture_url = %s,
                        description = %s,
                        price = %s
                        WHERE id = %s

                        """,
                        [
                            menu_item.category,
                            menu_item.name,
                            menu_item.picture_url,
                            menu_item.description,
                            menu_item.price,
                            menu_item_id,
                        ],
                    )
                    old_data = menu_item.dict()
                    return MenuItemOut(id=menu_item_id, **old_data)
        except Exception as e:
            print(e)
            return {"message": "Could not update menu item."}

    def list_menu_items(self) -> Union[Error, List[MenuItemOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, category, name, picture_url, description, price
                        FROM menu_items
                        ORDER BY id
                        """
                    )
                    return [
                        self.record_to_menu_item_out(record)
                        for record in result
                    ]

        except Exception as e:
            print(e)
            return {"message": "Could not list menu items."}

    def create(self, menu_item: MenuItemIn) -> MenuItemOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO menu_items
                            (category, name, picture_url, description, price)
                        VALUES
                            (%s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            menu_item.category,
                            menu_item.name,
                            menu_item.picture_url,
                            menu_item.description,
                            menu_item.price,
                        ],
                    )
                    id = result.fetchone()[0]
                    old_data = menu_item.dict()
                    return MenuItemOut(id=id, **old_data)

        except Exception as e:
            print(e)
            return {"message": "Could not create menu item."}

    def record_to_menu_item_out(self, record):
        return MenuItemOut(
            id=record[0],
            category=record[1],
            name=record[2],
            picture_url=record[3],
            description=record[4],
            price=record[5],
        )
