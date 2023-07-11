from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool


class Error(BaseModel):
    message: str


class MenuIn(BaseModel):
    category: str
    name: str
    picture: Optional[str]
    description: str


class MenuOut(BaseModel):
    id: int
    category: str
    name: str
    picture: Optional[str]
    description: str


class MenuRepository:
    def get_menu_item(self, menu_id: int) -> Optional[MenuOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, category, name, picture, description
                        FROM menu
                        WHERE id = %s
                        """,
                        [menu_id],
                    )
                    record = result.fetchone()
                    return self.record_to_menu_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not retrieve item info."}

    def delete(self, menu_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM menu
                        WHERE id = %s
                        """,
                        [menu_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(
        self, menu_id: int, menu: MenuIn
    ) -> Union[Error, List[MenuOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE menu
                        SET category = %s,
                        name = %s,
                        picture = %s,
                        description = %s
                        WHERE id = %s

                        """,
                        [
                            menu.category,
                            menu.name,
                            menu.picture,
                            menu.description,
                            menu_id,
                        ],
                    )
                    old_data = menu.dict()
                    return MenuOut(id=menu_id, **old_data)
        except Exception as e:
            print(e)
            return {"message": "Could not update menu item."}

    def list_menu(self) -> Union[Error, List[MenuOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, category, name, picture, description
                        FROM menu
                        ORDER BY id
                        """
                    )
                    return [
                        self.record_to_menu_out(record) for record in result
                    ]

        except Exception as e:
            print(e)
            return {"message": "Could not list menu items."}

    def create(self, menu: MenuIn) -> MenuOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO menu
                            (category, name, picture, description)
                        VALUES
                            (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            menu.category,
                            menu.name,
                            menu.picture,
                            menu.description,
                        ],
                    )
                    id = result.fetchone()[0]
                    old_data = menu.dict()
                    return MenuOut(id=id, **old_data)

        except Exception as e:
            print(e)
            return {"message": "Could not create menu item."}

    def record_to_menu_out(self, record):
        return MenuOut(
            id=record[0],
            category=record[1],
            name=record[2],
            picture=record[3],
            description=record[4],
        )
