steps = [
    [
        ## Create the table
        """
        CREATE TABLE order (
            id SERIAL PRIMARY KEY NOT NULL,
            menu_item_id SERIAL NOT NULL,
            category VARCHAR(50) NOT NULL,
            quantity VARCHAR (20) NOT NULL,
            price_usd NUMERIC (6,2) NOT NULL
         );
        """,
        ## Drop the table
        """
        DROP TABLE orders;
        """,
    ]
]
            # mozzarella_sticks BOOL,
            # disco_fries BOOL,
            # buffalo_wings BOOL,
            # onion_rings BOOL,
            # artichoke_dip BOOL,
            # coke BOOL,
            # green_tea BOOL,
            # coffee BOOL,
            # cold_brew BOOL,
            # vanilla_milkshake BOOL,
            # chocolate_milkshake BOOL,
            # oreo_milkshake BOOL,
            # cheeseburger BOOL,
            # double_cheeseburger BOOL,
            # grilled_cheese BOOL,
            # chicken_club BOOL,
            # chicken_tenders BOOL,
            # tuna_melt BOOL,
            # fries BOOL,
            # house_salad BOOL,
            # cherry_pie BOOL,
            # key_lime_pie BOOL,
            # vanilla_gelato BOOL
