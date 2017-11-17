DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS pub_auth;
DROP TABLE IF EXISTS publication;
DROP TABLE IF EXISTS article;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS incollection;
DROP TABLE IF EXISTS proceedings;
DROP TABLE IF EXISTS inproceedings;

CREATE TABLE author(
    name VARCHAR(500) PRIMARY KEY,
    last_name VARCHAR(100)
);

CREATE TABLE pub_auth(
    pub_key VARCHAR(100),
    author VARCHAR(500),
    PRIMARY KEY(pub_key, author)
);

CREATE TABLE publication(
    pub_key VARCHAR(100) PRIMARY KEY,
    pub_class VARCHAR(100),
    pub_type VARCHAR(100),
    title_abbrev VARCHAR(100),
    title VARCHAR(1000),
    year INTEGER,
    month INTEGER
);

CREATE TABLE article(
    pub_key VARCHAR(100) PRIMARY KEY,
    volume VARCHAR(100),
    journal VARCHAR(500),
    number VARCHAR(100)
);

CREATE TABLE book(
    pub_key VARCHAR(100) PRIMARY KEY,
    publisher VARCHAR(500),
    series VARCHAR(100),
    volume VARCHAR(100)
);

CREATE TABLE incollection(
    pub_key VARCHAR(100) PRIMARY KEY,
    booktitle VARCHAR(500)
);

CREATE TABLE proceedings(
    pub_key VARCHAR(100) PRIMARY KEY,
    booktitle VARCHAR(500),
    publisher VARCHAR(500)
);

CREATE TABLE inproceedings(
    pub_key VARCHAR(100) PRIMARY KEY,
    booktitle VARCHAR(500)
);

DROP VIEW IF EXISTS year7079 ;
DROP VIEW IF EXISTS year8089 ;
DROP VIEW IF EXISTS year9099 ;
DROP VIEW IF EXISTS year0009 ;
DROP VIEW IF EXISTS year1019 ;

CREATE VIEW year7079 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=1970 and 
            year <=1979 and 
            pub_class = 'inproceedings'
);

CREATE VIEW year8089 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=1980 and 
            year <=1989 and 
            pub_class = 'inproceedings'
);

CREATE VIEW year9099 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=1990 and 
            year <=1999 and 
            pub_class = 'inproceedings'
);

CREATE VIEW year0009 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=2000 and 
            year <=2009 and 
            pub_class = 'inproceedings'
);

CREATE VIEW year1019 AS(
    SELECT  count(pub_key) as cnt
    FROM    publication
    WHERE   year >=2010 and 
            year <=2019 and 
            pub_class = 'inproceedings'
);

DROP VIEW IF EXISTS collaborators;

CREATE VIEW collaborators AS(
    SELECT  a.author as author, count(a.author) as cnt
    FROM    pub_auth a, pub_auth b
    WHERE   a.author <> b.author AND 
            a.pub_key = b.pub_key AND
            a.pub_key IN (
                SELECT  pub_key
                FROM    publication
                WHERE   (pub_class = 'inproceedings' OR pub_class = 'article') AND
                        lower(title) LIKE '%data%' 
            )
    GROUP BY a.author
);