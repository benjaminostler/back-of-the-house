from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union, Optional


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

    def update(
        self,
        order_items_id: int,
        order_items: OrderItemsIn
    ) -> Union[OrderItemsOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE order_items
                        SET
                            orders_id = %s,
                            menu_item_id = %s,
                            quantity = %s,
                        WHERE id = %s

                        """,
                        [
                            order_items.orders_id,
                            order_items.menu_item_id,
                            order_items.quantity,
                            order_items_id,
                        ]
                    )
                    order_items.id = order_items_id
                    return order_items
        except Exception as e:
            print(e)
            return {"message": "Could not update order items."}

    def get_order_item(self, order_items_id: int) -> Optional[OrderItemsOut]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id,
                            menu_item_id,
                            quantity
                        FROM order_items
                        WHERE id = %s
                        """,
                        [order_items_id]
                    )
                    record = db.fetchone()[0]
                    if record is None:
                        return {"message": "Order item not found"}
                    return self.record_to_order_items_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that order item"}

    # def get_order_items(self) -> Union[List[OrderItemsOut], Error]:
    #     # Shows a single menu item, the quantity of it in a particular order
    #     try:
    #         with pool.connection() as conn:
    #             with conn.cursor() as db:
    #                 result = db.execute(
    #                     """
    #                     SELECT id,
    #                         orders_id,
    #                         menu_item_id,
    #                         quantity
    #                     FROM order_items;
    #                     """
    #                 )
    #                 # LEFT JOIN orders
    #                 # on order_items.orders_id=orders.id
    #                 # ORDER BY orders.id;
    #                 return [
    #                     self.record_to_order_items_out(record)
    #                     for record in result
    #                 ]
    #     except Exception:
    #         return {"message": "Could not get all order items"}

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

    def delete(self, order_item_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM order_items
                        WHERE id = %s
                        """,
                        [order_item_id],
                    )
            return True
        except Exception as e:
            print(e)
            return False

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
