

DROP TABLE IF EXISTS auth;
CREATE TABLE auth (
    authid INTEGER PRIMARY KEY,
    name   TEXT,
    birth  TEXT
);

BEGIN TRANSACTION;

    INSERT INTO auth ( authid, name, birth ) VALUES ( 1, 'bob', '1970.05.01' );
    INSERT INTO auth ( authid, name, birth ) VALUES ( 2, 'kim', '1980.05.01' );
    INSERT INTO auth ( authid, name, birth ) VALUES ( 7, 'park', '2000.05.01' );

    -- ROLLBACK TRANSACTION;

COMMIT TRANSACTION ;

SELECT * FROM auth;



-- book table
DROP TABLE IF EXISTS book;
CREATE TABLE book (
    book_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    title     TEXT,
    publisher TEXT,
    year      TEXT,
    price     INTEGER,
    dtm       TEXT,
    use_yn    INTEGER,
    authid    INTEGER
);

BEGIN TRANSACTION;

    INSERT INTO book ( title, publisher, year, price, dtm, use_yn, authid ) VALUES ( 'Operating System', 'Wiley', '2003', 30700, '2004-01-01', 0, 1 );
    INSERT INTO book ( title, publisher, year, price, dtm, use_yn, authid ) VALUES ( 'MySQL', 'OReilly', '2009', 58700, '2010-01-01', 1, 2 );
    INSERT INTO book ( title, publisher, year, price, dtm, use_yn, authid ) VALUES ( 'JAVA', 'Hall', '2013', 40000, '2014-01-01', 1, 3 );
    INSERT INTO book ( title, publisher, year, price, dtm, use_yn, authid ) VALUES ( 'First SQL', 'Wiley', '2015', 57700, '2016-01-01', 1, 4 );

    -- ROLLBACK TRANSACTION;

COMMIT TRANSACTION ;

SELECT * FROM book;



-- phonebook table
DROP TABLE IF EXISTS phonebook;
CREATE TABLE phonebook (
    Name     TEXT,
    PhoneNum TEXT
);


BEGIN TRANSACTION;
    INSERT INTO PhoneBook(Name, PhoneNum) VALUES('Derick','010-1234-5678');
    INSERT INTO PhoneBook(Name, PhoneNum) VALUES('Tom','010-543-5432');
    INSERT INTO PhoneBook(Name, PhoneNum) VALUES('DSP','010-123-1234');


    -- ROLLBACK  TRANSACTION;

COMMIT  TRANSACTION;


SELECT *   FROM PhoneBook;
