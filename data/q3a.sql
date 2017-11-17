SELECT  *
FROM    publication 
WHERE   year = 2015 AND pub_key IN (
    SELECT  pub_key
    FROM    pub_auth
    WHERE   author = 'Hongli Xu'
);