SELECT  *
FROM    publication 
WHERE pub_key IN (
    SELECT  pub_key
    FROM    pub_auth
    WHERE   author = 'Hongli Xu'
) AND year = 2015 AND title_abbrev = 'wasa';