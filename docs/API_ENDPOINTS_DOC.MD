# Team Gastronauts : Gastronomical Gems

- (Local Backend): http://localhost:8000/docs
- (Local Frontend): http://localhost:3000
<br>

## SQL Table - Accounts
```SQL
CREATE TABLE accounts (
            id              SERIAL PRIMARY KEY NOT NULL,
            first_name      VARCHAR(1000) NOT NULL,
            last_name       VARCHAR(100) NOT NULL,
            username        VARCHAR(100) NOT NULL,
            hashed_password VARCHAR(100) NOT NULL,
            email           VARCHAR(100) NOT NULL,
            phone_number    VARCHAR(100) NOT NULL
        );
```
## SQL Table - Menu Items
```SQL
CREATE TABLE menu_items (
            id          SERIAL PRIMARY KEY not null,
            category    VARCHAR(30) not null,
            name        VARCHAR(100) not null,
            picture_url TEXT,
            description TEXT,
            price       NUMERIC(8,2) not null
        );
```
## SQL Table - Orders
```SQL
CREATE TABLE orders (
            id              SERIAL PRIMARY KEY NOT NULL,
            account_id      INT NOT NULL,
            subtotal        NUMERIC (6,2) NOT NULL,
            total           NUMERIC (6,2) NOT NULL,
            FOREIGN KEY (account_id)
                REFERENCES accounts (id)
        );
```
## SQL Table - Order Items
```SQL
CREATE TABLE order_items (
            id              SERIAL PRIMARY KEY NOT NULL,
            orders_id       INT NOT NULL,
            menu_item_id    INT NOT NULL,
            quantity        INT,
            FOREIGN KEY (menu_item_id)
                REFERENCES menu_items (id)
        );
```
## SQL Table - Reservations
```SQL
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

```
## SQL Table - Cart
```SQL
CREATE TABLE cart (
            id          SERIAL PRIMARY KEY not null,
            total_price NUMERIC(6,2)
        );
```
## SQL Table - Cart Items
```SQL
CREATE TABLE cart_items (
            id          SERIAL PRIMARY KEY not null,
            cart_id     INT not null,
            menu_item_id    INT not null,
            quantity    INT not null,
            FOREIGN KEY (cart_id)
                REFERENCES cart (id),
            FOREIGN KEY (menu_item_id)
                REFERENCES menu_items (id)
        );
```
<br>

# ENDPOINTS
<br>

#### Get All Users
**REQUEST METHOD:** GET

**PATH:** /api/accounts/

## **REQUEST BODY:**
None

## **Response Shape**
**200 - Success**
```json
[
  {
    "id": 1,
    "first_name": "asdfasdfasdfasdfasdfasdfasdfasdfasdf",
    "last_name": "asdf",
    "username": "asdf",
    "hashed_password": "$2b$12$rYh.QfHcBXc/GT2DMj13HO.HapegTdzUCM9I/IZ5bU309kFrT48qO",
    "email": "asdf@asdf.com",
    "phone_number": "1234"
  },
  {
    "id": 2,
    "first_name": "JohnUpdated",
    "last_name": "Doe",
    "username": "johndoe",
    "hashed_password": "hashed_password",
    "email": "johndoe@example.com",
    "phone_number": "1234567890"
  },...
```
