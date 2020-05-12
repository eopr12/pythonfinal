

-- @@@@@@@@@@@@@@@@@@@@
-- 학습 주제
-- 1. 주석
-- 2. DML 기본 구문
--    select 컬럼명1, 컬럼명2, ...
--    from 테이블명
--    where 1 = 1
--    order by 컬럼명1, 컬럼명2, ...
-- 3. DML CRUD2s
--      Create    <==> insert
--      Read      <==> select
--      Update    <==> update
--      Delete    <==> delete
--      Search    <==> where
--      Sort      <==> order by
-- @@@@@@@@@@@@@@@@@@@@


-- ####################
-- Read 방법 : select 문 사용
-- ####################

SELECT * FROM book;

SELECT title,  publisher,  price,  authid  FROM book;


-- ####################
-- Search 방법  <==> where 문 사용
-- ####################

SELECT * FROM book  WHERE title like '%SQL%';

SELECT * FROM book  WHERE title = 'JAVA';

SELECT * FROM book  WHERE 30700 <= price and price <50000;

SELECT * FROM book  WHERE price BETWEEN 30700 AND 50000;

SELECT * FROM book  WHERE price <= 30700 OR 58000 < price ;


-- ####################
-- Sort 방법. order by 문 사용.
-- ####################

SELECT * FROM book;

SELECT * FROM book ORDER BY price ASC;

SELECT * FROM book ORDER BY price DESC;

SELECT * FROM book ORDER BY publisher ASC, price DESC;


-- ####################
-- Create 방법. insert 문 사용.
-- ####################

SELECT * FROM book;

INSERT INTO book (title   , publisher, year  , price, authid )
            VALUES('System', 'Wiley'  , '2003', 30700, 1      ) ;

SELECT * FROM book;


SELECT * FROM auth;
            
INSERT INTO auth  (authid, name  , birth        )
            VALUES(8     , 'bob' , '1970.05.01' ) ;

SELECT * FROM auth;


-- ####################
-- Update 방법. update 문 사용
-- ####################

SELECT * FROM book WHERE  title like '%SQL%' ;
UPDATE  book
   SET  year = '2016'
WHERE  title like '%SQL%' ;
SELECT * FROM book WHERE  title like '%SQL%' ;


SELECT * FROM book WHERE  title = 'JAVA' ;
UPDATE  book
   SET  year = '2010'
     ,  price = 20000
WHERE  title = 'JAVA' ;
SELECT * FROM book WHERE  title = 'JAVA' ;


-- ####################
-- Delete 방법. delete 문 사용
-- ####################
SELECT * FROM book WHERE  title = 'JAVA' ;
DELETE FROM book
      WHERE title = 'JAVA' ;
SELECT * FROM book WHERE  title = 'JAVA' ;


SELECT * FROM book WHERE publisher ='Wiley' AND year < '2015'  ;
DELETE FROM book WHERE publisher ='Wiley' AND year < '2015'  ;
SELECT * FROM book WHERE publisher ='Wiley' AND year < '2015'  ;


-- @@@@@@@@@@@@@@@@@@@@
-- 조인이란 테이블을 연결하는 방법이다.
--
-- 조인의 종류
-- 교집합 : inner join  ==>
-- 합집합(좌측 기준) : left join  = left outer join
-- 합집합(우측 기준)right join = right outer join
-- cross join
-- @@@@@@@@@@@@@@@@@@@@


-- ####################
-- inner  join
-- ####################
select book.*, auth.*
  from book
  inner join auth on book.authid = auth.authid ;


-- ####################
-- left join
-- ####################
select book.*, auth.*
  from book
  left join auth on book.authid = auth.authid ;


