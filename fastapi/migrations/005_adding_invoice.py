steps = [
    [
        ## Create the table
        """
        CREATE TABLE invoice (
            id SERIAL PRIMARY KEY NOT NULL,
            order_id SERIAL NOT NULL,
            subtotal NUMERIC (6,2) NOT NULL,
            total NUMERIC(6,2) NOT NULL


        );
        """,
        ## Drop the table
        """
        DROP TABLE invoice;
        """,
    ]
]
