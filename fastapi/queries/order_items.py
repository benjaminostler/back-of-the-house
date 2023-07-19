from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union


class Error(BaseModel):
    message: str


class OrderItemsIn(BaseModel):
    orders_id: int
    menu_item_id: int
    quantity: int


class OrderItemsOut(BaseModel):
    id: int
    orders_id: int
    menu_item_id: int
    quantity: int


class OrderItemsRepository(BaseModel):

    def get_all(self) -> Union[List[OrderItemsOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id,
                            orders_id,
                            menu_item_id,
                            quantity
                        FROM order_items
                        ORDER BY id
                        """
                    )
                    return [
                        self.record_to_order_items_out(record)
                        for record in result
                    ]
        except Exception:
            return {"message": "Could not get all order items"}

    def create(self, order_items: OrderItemsIn) -> OrderItemsOut:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO order_items
                            (
                            orders_id
                            , menu_item_id
                            , quantity
                            )
                        VALUES
                            (%s, %s, %s)
                        RETURNING id
                        """,
                        [
                            order_items.orders_id,
                            order_items.menu_item_id,
                            order_items.quantity
                        ]
                    )
                    id = result.fetchone()[0]
                    return self.order_items_in_to_out(id, order_items)
        except Exception as e:
            print("e", e)
            return {"message": "Could not create new order items."}

    def order_items_in_to_out(self, id: int, order_items: OrderItemsIn):
        old_data = order_items.dict()
        return OrderItemsOut(id=id, **old_data)

    def record_to_order_items_out(self, record):
        return OrderItemsOut(
            id=record[0],
            orders_id=record[1],
            menu_item_id=[2],
            quantity=[3],
        )
