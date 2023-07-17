steps = [
    [
        """
        CREATE TABLE menu_item (
            id SERIAL PRIMARY KEY not null,
            category VARCHAR(30) not null,
            name VARCHAR(100) not null,
            picture_url TEXT,
            description TEXT not null,
            price NUMERIC(8,2) not null
        );

        """,
        """
        DROP TABLE menu_item;

        """,
    ]
]
