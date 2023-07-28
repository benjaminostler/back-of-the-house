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

    def get_all(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT *
                    FROM order_items
                    """
                )

                record = db.fetchall()
                return self.record_to_all_order_items_out(record)



    # def get_order_item_detail(self, order_items_id: int,) -> Optional[OrderItemsOut]:
    #     try:
    #         # connect the database
    #         with pool.connection() as conn:
    #             # get a cursor (something to run SQL with)
    #             with conn.cursor() as db:
    #                 db.execute(
    #                     """
    #                     SELECT id,
    #                         orders_id,
    #                         menu_item_id,
    #                         quantity
    #                     FROM order_items
    #                     WHERE id = %s
    #                     """,
    #                     [order_items_id]

    #                 )
    #                 record = db.fetchone()
    #                 print("get_order_item_detail",record)
    #                 if record is None:
    #                     return {"message": "Order not found"}
    #                 return self.record_to_order_items_out(record)
    #     except Exception as e:
    #         print(e)
    #
    #
    #        return {"message": "Could not get that order"}

    def get_order_item_detail(self, order_items_id: int):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT * FROM order_items
                    WHERE id = %s
                    """,
                    [order_items_id],
                )
                record = db.fetchone()
                return self.record_to_order_items_out(record)





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

    def delete(self, orders_item_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM order_items
                        WHERE id = %s
                        """,
                        [orders_item_id],
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

    def record_to_all_order_items_out(self, records):
        order_items = []
        for record in records:
            order_items.append(
                OrderItemsOut(
                 id=record[0],
                 orders_id=record[1],
                 menu_item_id=record[2],
                 quantity=record[3],

                )

            )
        return order_items
