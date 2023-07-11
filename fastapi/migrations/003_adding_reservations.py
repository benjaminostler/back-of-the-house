steps = [
    [
        ## Create the table
        """
        CREATE TABLE reservations (
            id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(1000) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            phone_number VARCHAR(100) NOT NULL,
            email_address VARCHAR(100) NOT NULL,
            party_size VARCHAR(100) NOT NULL,
            date VARCHAR(100) NOT NULL,
            time VARCHAR(100) NOT NULL
        );
        """,
        ## Drop the table
        """
        DROP TABLE reservations;
        """,
    ]
]
