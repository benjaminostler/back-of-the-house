steps = [
    [
        ## Create the table
        """
        CREATE TABLE orders (
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