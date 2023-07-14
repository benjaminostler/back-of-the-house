steps = [
    [
        ## Create the table
        """
        CREATE TABLE invoice (
            id SERIAL PRIMARY KEY NOT NULL,
            order_id INT NOT NULL,
            subtotal NUMERIC (6, 2) NOT NULL,
            total NUMERIC (6, 2) NOT NULL,
            FOREIGN KEY (order_id)
                REFERENCES orders (id)
        );
        """,
        ## Drop the table
        """
        DROP TABLE invoice;
        """,
    ]
]