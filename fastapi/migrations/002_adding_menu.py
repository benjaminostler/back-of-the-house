steps = [
    [
        """
        create table menu (
            id serial primary key not null,
            category varchar(30) not null,
            name varchar(100) not null,
            picture text not null,
            description text not null

        );

        """,
        """
        drop table menu;

        """,
    ]
]
