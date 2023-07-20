steps = [
    # Create the tables
    [

        """
        CREATE TABLE accounts (
            id              SERIAL PRIMARY KEY NOT NULL,
            first_name      VARCHAR(1000) NOT NULL,
            last_name       VARCHAR(100) NOT NULL,
            username        VARCHAR(100) NOT NULL,
            hashed_password VARCHAR(100) NOT NULL,
            email           VARCHAR(100) NOT NULL,
            phone_number    VARCHAR(100) NOT NULL
        );
        """,
        """
        DROP TABLE accounts;
        """
    ],
    [
        """
        CREATE TABLE menu_items (
            id          SERIAL PRIMARY KEY not null,
            category    VARCHAR(30) not null,
            name        VARCHAR(100) not null,
            picture_url TEXT,
            description TEXT,
            price       NUMERIC(8,2) not null
        );
        """,
        """
        DROP TABLE menu_items;
        """
    ],
    [
        """
        CREATE TABLE orders (
            id              SERIAL PRIMARY KEY NOT NULL,
            account_id      INT NOT NULL,
            subtotal        NUMERIC (6,2) NOT NULL,
            total           NUMERIC (6,2) NOT NULL,
            FOREIGN KEY (account_id)
                REFERENCES accounts (id)
        );
        """,
        """
        DROP TABLE orders;
        """
    ],
    [
        """
        CREATE TABLE order_items (
            id              SERIAL PRIMARY KEY NOT NULL,
            orders_id       INT NOT NULL,
            menu_item_id    INT NOT NULL,
            quantity        INT NOT NULL,
            FOREIGN KEY (menu_item_id)
                REFERENCES menu_items (id)
        );
        """,
        """
        DROP TABLE order_items;
        """
    ],
    [
        """
        CREATE TABLE reservations (
            id              SERIAL PRIMARY KEY NOT NULL,
            account_id      INT NOT NULL,
            first_name      VARCHAR(1000) NOT NULL,
            last_name       VARCHAR(100) NOT NULL,
            email           VARCHAR(100) NOT NULL,
            phone_number    VARCHAR(100) NOT NULL,
            party_size      VARCHAR(100) NOT NULL,
            date            VARCHAR(100) NOT NULL,
            time            VARCHAR(100) NOT NULL,
            FOREIGN KEY (account_id)
                REFERENCES accounts (id)
        );
        """,
        """
        DROP TABLE reservations;
        """
    ]
]
