
    def record_to_order_items_out(self, record):
        return OrderItemsOut(
            id=record[0],
            orders_id=record[1],
            menu_item_id=[2],
            quantity=[3],
        )