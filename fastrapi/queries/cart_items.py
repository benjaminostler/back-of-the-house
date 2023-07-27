from pydantic import BaseModel
from typing import Union, List
from queries.pool import pool


class Error(BaseModel):
    message: str


class CartItemIn(BaseModel):
    cart_id: int
    menu_item_id: int
    quantity: int


class CartItemOut(BaseModel):
    id: int
    cart_id: int
    menu_item_id: int
    picture_url: str
    price: float
    quantity: int


class CartItemRepository:
    def list_cart_items(self) -> Union[List[CartItemOut], Error]:
        query = """
            SELECT cart_items.id, cart_items.cart_id, cart_items.menu_item_id,
                menu_items.picture_url, menu_items.price, cart_items.quantity
            FROM cart_items
            INNER JOIN menu_items ON cart_items.menu_item_id = menu_items.id;
        """
        try:
            with pool.connection() as conn:
                result = conn.execute(query)
                return [
                    self.record_to_cart_item_out(record)
                    for record in result.fetchall()
                ]
        except Exception as e:
            print(e)
            return {"message": "Failed to list cart items."}

    def get_cart_item(self, cart_item_id: int) -> Union[CartItemOut, Error]:
        query = """
            SELECT cart_items.id, cart_items.cart_id, cart_items.menu_item_id,
                menu_items.picture_url, menu_items.price, cart_items.quantity
            FROM cart_items
            INNER JOIN menu_items ON cart_items.menu_item_id = menu_items.id
            WHERE cart_items.id = :id;
        """
        try:
            with pool.connection() as conn:
                result = conn.execute(query, {"id": cart_item_id}).fetchone()
                return self.record_to_cart_item_out(result)
        except Exception as e:
            print(e)
            return {"message": "Failed to get cart item."}

    def update_quantity(
        self, cart_item_id: int, quantity: int
    ) -> Union[CartItemOut, Error]:
        update_query = """
            UPDATE cart_items
            SET quantity=:quantity
            WHERE id=:id
            RETURNING id, cart_id, menu_item_id, quantity;
        """

        get_query = """
            SELECT cart_items.id, cart_items.cart_id, cart_items.menu_item_id,
                menu_items.picture_url, menu_items.price, cart_items.quantity
            FROM cart_items
            INNER JOIN menu_items ON cart_items.menu_item_id = menu_items.id
            WHERE cart_items.id = :id;
        """

        try:
            with pool.connection() as conn:
                result = conn.execute(
                    update_query, {"quantity": quantity, "id": cart_item_id}
                )
                updated_cart_item = result.fetchone()

                result = conn.execute(
                    get_query, {"id": updated_cart_item["id"]}
                )
                updated_cart_item_full = result.fetchone()

                return self.record_to_cart_item_out(updated_cart_item_full)

        except Exception as e:
            print(e)
            return {"message": "Failed to update cart item quantity."}

    def delete(self, cart_item_id: int) -> Union[str, Error]:
        query = """
            DELETE FROM cart_items
            WHERE id=:id;
        """
        try:
            with pool.connection() as conn:
                conn.execute(query, {"id": cart_item_id})
                return {"message": "Successfully deleted cart item."}

        except Exception as e:
            print(e)
            return {"message": "Failed to delete cart item."}

    def record_to_cart_item_out(self, record):
        return CartItemOut(
            id=record[0],
            cart_id=record[1],
            menu_item_id=record[2],
            picture_url=record[3],
            price=record[4],
            quantity=record[5],
        )
