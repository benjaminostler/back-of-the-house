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
2. We all committed our changes to the main branch and ran into errors with the order and order_items endpoints. Alec, Ray, and I spent a long time with resolving conflicts in our merges and problem solving. Part of the solution I discovered was to remove the order_items_id from the orders table, which removed the circular dependency. I spent a long time updating the code and ran into issues with "duplicate operation IDs" in routers. Destroying and rebuilding the database, images, and containers. Then we ran into an error that in the order_items endpoint get_all said that menu_item_id and quantity were not of required type integer.
3. I replaced the get_all endpoint with a get_one endpoint since the order_items table is only intended to track one menu_item at a time and its quantity. After that we still had the integer error from the previous day. Ray helped me with fixing that by adding "[0]" to the fetchone line in queries.

## Week 16 (July 24th - July 28th)

1. We caught each other up on progress and assigned which team members would be working on which front end pages. Alec and I teamed up since my page will rely on his page. Ed finished our deployment of front and back end. Alec and I each wrote the basic code for our pages. He wrote the code for the list menu items page and I wrote the code for the create menu item page. We didn't get them to work yet though. My docker app was giving me issues for the last couple hours of the day so I couldn't test my code.
2. Alec and I worked together all morning to figure out how to get a request in our app.js to work with our database so we could use it as a prop to list menu items and etc. I created and followed the console log trail and discovered the getMenuItems request in app.js was setting menuItems as undefined. I fixed the problem by changing the code from setMenuItems(data.menuItems) to setMenuItems(data). There was no such thing as data.menuItems because the keys in the returned data were 1, 2, etc. Now the list menu items page successfully show the table of existing menu items! After lunch, I wrote all of the code for the create menu item page which contains a form for submission. I got it to successfully several new menu items to the database.
3. I submitted a merge request and got it to pass the pipeline tests. I helped Alec do the same. Then we worked on the bootstrap styling for the menu_items page and create menu item page. We ran into CORS errors when trying to create accounts and when trying to create menu items on the deployed front end. I created a custom Zoom background on Canva.com for our group members to use.
4. Ed created a shopping cart and pushed it to main. We worked hard on trying to fix several CORS errors on the deployed site on our various requests. Even though we got some guidance from Rosheen it did not fix the problem. We also got another error called Mixed content about needing to request a secure resource from a secure resource. We made a lot of progress on front end. I made a lot of progress on creating the order history page locally. Ed said he would work on creating a complete order button at the end of the cart that creates an entry in the orders table so I can use the entries on the order history page.
5. Edited and uploaded background video for main page. Wrote basic Orders unit test and it passed. Fixed the Nav bar to only show the appropriate nav links once someone is logged in. I created a "create order" page and so I got both the create order page and the order history page to work. I got started on the readme and added the ERD link, Wireframe link, and FastAPI links. I made a list of what part of the project each team member did so we can get appropriate credit.
