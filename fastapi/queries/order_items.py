# Raymond:
# get one
# delete
# Benjamin:
# create
# get all
from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union, Optional


class Error(BaseModel):
    message: str


class OrderItemsIn(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int


class OrderItemsOut(BaseModel):
    id: int
    order_id: int
    menu_item_id: int
    quantity: int


class OrderItemsRepository(BaseModel):

    def get_order_items(self, order_item_id: int) -> Optional[OrderItemsOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, order_id, menu_item_id, quantity
                        FROM order_items
                        WHERE id = %s
                        """,
                        [order_item_id],
                    )
                    record = result.fetchone()
                    return self.record_to_order_item_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not retrieve this item."}

    def list_order_items(self) -> Union[Error, List[OrderItemsOut]]:
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
                            orders_id,
                            menu_item_id,
                            quantity
                            )
                        VALUES
                            (%s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            order_items.order_id,
                            order_items.menu_item_id,
                            order_items.quantity
                        ]
                    )
                    id = result.fetchone()[0]
                    # Return new data
                    return self.order_items_in_to_out(id,  order_items)
        except Exception as e:
            print("e", e)
            return {"message": "Could not create new order items list."}

    def update(
        self, order_items_id: int, order_items: OrderItemsIn
    ) -> Union[Error, List[OrderItemsOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE order_items
                        SET
                            order_id,
                            menu_item_id,
                            quantity,
                        WHERE id = %s

                        """,
                        [
                            order_items.order_id,
                            order_items.menu_item_id,
                            order_items.quantity
                        ]
                    )
                    old_data = order_items.dict()
                    return OrderItemsOut(id=order_items_id, **old_data)
        except Exception as e:
            print(e)
            return {"message": "Could not update order items."}
        
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