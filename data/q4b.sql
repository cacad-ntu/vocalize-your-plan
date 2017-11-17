SELECT DISTINCT tmp_a.author 
FROM (
    SELECT a.author as author, count(a.author) as cnt
    FROM pub_auth AS a, publication AS b
    WHERE b.title_abbrev = 'pvldb' AND a.pub_key = b.pub_key
    GROUP BY a.author
) as tmp_a
WHERE tmp_a.cnt >= 15 AND tmp_a.author NOT IN (
    SELECT a.author as author
    FROM pub_auth AS a, publication AS b
    WHERE b.title_abbrev = 'kdd' AND a.pub_key = b.pub_key
    GROUP BY a.author
);