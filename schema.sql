
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS recieve_loc;
DROP TABLE IF EXISTS donation_loc;
DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS auth;
CREATE TABLE person (
    p_id INTEGER PRIMARY KEY ,
    p_name TEXT NOT NULL,
    p_gender TEXT NOT NULL,
    p_blood_grp TEXT  NOT NULL,
    p_address VARCHAR(100) NOT Null,
    p_dob DATE NOT NULL
);

CREATE TABLE donation_loc (
    date_of_don DATETIME NOT NULL,
    quantity INTEGER NOT NULL,
    p_id INTEGER NOT NULL,
    FOREIGN KEY (p_id) REFERENCES person(p_id)

);

CREATE TABLE auth(
    username varchar(20) PRIMARY KEY,
    passw varchar(20) NOT NULL
);
CREATE TABLE recieve_loc (
    r_date DATETIME NOT NULL,
    quantity INTEGER NOT NULL,
    p_id INTEGER NOT NULL,
    FOREIGN KEY (p_id) REFERENCES person(p_id)

);

CREATE TABLE stock(
    s_blood_grp VARCHAR(4) PRIMARY KEY,
    quantity INTEGER
);