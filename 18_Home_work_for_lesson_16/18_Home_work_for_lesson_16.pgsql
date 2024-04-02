-- 1. Write SQL queries for table creation for a data model that you created for prev homework (Airbnb model)

CREATE TABLE users(
    user_id INTEGER PRIMARY KEY,
    user_name varchar(50) NOT NULL,
    user_email text,
    user_type text
);


CREATE TABLE rooms(
    room_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount_of_residens INTEGER,
    price INTEGER,
    located text,
    availiability text
);


CREATE TABLE reservations(
    reservation_id INTEGER PRIMARY KEY,
    start_date date,
    end_date date,
    user_id INTEGER,
    room_id INTEGER,
    if_paid text,
    reservated text
);


CREATE TABLE review(
    review_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    room_id INTEGER
);

-- 2. Write 3 rows (using INSERT queries) for each table in the data model

INSERT INTO users(user_id, user_name,user_email, user_type) VALUES (1, 'Iryna', 'iryna@gmil.com', 'host');
INSERT INTO users(user_id, user_name,user_email, user_type) VALUES (2, 'Pavel', 'pavel@gmil.com', 'guest');
INSERT INTO users(user_id, user_name,user_email, user_type) VALUES (3, 'Nazar', 'nazar@gmil.com', 'host');

SELECT * FROM users; 

INSERT INTO rooms(room_id, user_id, amount_of_residens, price, located, availiability) VALUES (1, 1, 2, 100, 'Madrid', 'Y');
INSERT INTO rooms(room_id, user_id, amount_of_residens, price, located, availiability) VALUES (2, 3, 4, 180, 'Venezia', 'Y');
INSERT INTO rooms(room_id, user_id, amount_of_residens, price, located, availiability) VALUES (3, 3, 3, 130, 'Stambul', 'N');

SELECT * FROM rooms;

INSERT INTO reservations(reservation_id, reservated) VALUES (1,'N');
INSERT INTO reservations(reservation_id, start_date, end_date, user_id, room_id, if_paid, reservated) VALUES (2, '2024-02-01', '2024-02-02', 2, 2, 'Y', 'Y');
INSERT INTO reservations(reservation_id, reservated) VALUES (3,'N');

SELECT * FROM reservations;

INSERT INTO review(review_id, user_id, room_id) VALUES (1, 2, 1);
INSERT INTO review(review_id, user_id, room_id) VALUES (2, 2, 2);
INSERT INTO review(review_id, user_id, room_id) VALUES (3, 2, 3);

SELECT * FROM review;

-- 3. Create the next analytic queries:
--       1. Find a user who had the biggest amount of reservations. Return user name and user_id
--       2. (Optional) Find a host who earned the biggest amount of money for the last month. Return hostname and host_id
--       3. (Optional) Find a host with the best average rating. Return hostname and host_id

SELECT u.user_name, u.user_id FROM users u
JOIN reservations r ON u.user_id = r.user_id
GROUP BY u.user_id, u.user_name
ORDER BY count(r.reservation_id)
DESC
LIMIT 1;


CREATE TABLE user_room(
    id_user_room INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,

FOREIGN KEY (user_id)
    REFERENCES users(user_id),
FOREIGN KEY (room_id)
    REFERENCES rooms(room_id)
    );

SELECT * FROM user_room;
  
-- ERROR: syntax error at or near "user_id"

-- v2
-- CREATE TABLE user_room(
--     id_user_room INTEGER PRIMARY KEY,
--     user_id INTEGER NOT NULL,
--     room_id INTEGER NOT NULL,

-- constraint fk_user_id FOREIGN KEY (user_id)
--     REFERENCES users(user_id),
-- constraint fk_room_id FOREIGN KEY (room_id)
--     REFERENCES rooms(room_id));