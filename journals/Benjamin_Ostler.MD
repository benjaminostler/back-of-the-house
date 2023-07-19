# Journal

## Week 13 (June 19th - June 23rd)

During this week, I worked on the following tasks:

1. I created ERD for the design of our restaurant app. https://drive.google.com/file/d/1pWQop7rLnYlZO-vijExYePNbFCZVOuoy/view?usp=sharing
2. I created a Scrum Board on Trello to manage tasks. https://trello.com/b/BuAWzC6F/restaurant-scrum-board
3. Ed worked hard and did a lot but he was working on his personal repository and did not copy his code to the group's repository. He told us to wait for him to copy it over before working on it so I wasn't able to run the app or work on it.
4. Kenny did a lot of work too but did not push his changes to main until later in the week which also made it difficult for me to contribute.

## Week 14 (June 26th - June 30th)

1. Ken finally pushed his changes to main:
   https://gitlab.com/backofthehouse/gastronomical-gems/-/merge_requests/1
2. Ed finally copied his work to our repository so we were able to clone and run fastapi & the react app. https://gitlab.com/backofthehouse/gastronomical-gems/-/merge_requests/2
3. I created my own branch and cloned the repository. Ed and Kenny helped me get the fastapi running, and use it to test completed endpoints. https://gitlab.com/backofthehouse/gastronomical-gems/-/merge_requests/9
4. I created my journal file and committed it to the repository. https://gitlab.com/backofthehouse/gastronomical-gems/-/merge_requests/14

## Week 15 (July 10th - July 14th)

1. Ed and Ken caught us up on things they had completed over the break.
2. I installed all of the coding software and etc on my laptop since I have been using my desktop until forced to use my laptop now.
3. Ed helped Alec create his journal file and commit it to the repository. https://gitlab.com/backofthehouse/gastronomical-gems/-/merge_requests/21
4. Alec, Raymond, and I worked together to create migration file for orders, then migrated the changes.
5. Alec, Raymond, and I split up the endpoints for invoices and orders between us to complete by the next day.

## Week 16 (July 17th - July 21st)

1. Worked with SEIRs (Rosheen and Zach) to get creation of tables to work. We removed the invoice table and created the "order_items" table instead as a way to have multiple items in an order. We also combined all of the table creation sql into the "001_adding_all_tables.py" file. In order to avoid the errors caused by circular references by the foreign keys of the order table and the order_items table, we left out the foreign key constraint on orders_id, then added a separate step at the end of the migration file with an ALTER TABLE to add the "orders_id" foreign key constraint to the order_items table now that all of the tables had been created, including the orders table, and there would be no reference error. Raymond and I created the query and router files for the new order_items table. It throws an error when trying to create because it says there is no order with the specified orders_id and no menu_item with the menu_item_id. This means we will have to wait for Alec and Edward to finish updating their queries and routers for orders and menu_items.
2.
