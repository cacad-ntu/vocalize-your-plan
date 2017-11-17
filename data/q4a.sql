SELECT DISTINCT tmp_a.author 
FROM (
    SELECT a.author as author, count(a.author) as cnt
    FROM pub_auth AS a, publication AS b
    WHERE b.title_abbrev = 'pvldb' AND a.pub_key = b.pub_key
    GROUP BY a.author
) as tmp_a, (
    SELECT a.author as author, count(a.author) as cnt
    FROM pub_auth AS a, publication AS b
    WHERE b.title_abbrev = 'sigmod' AND a.pub_key = b.pub_key
    GROUP BY a.author
) as tmp_b
WHERE tmp_a.cnt >= 10 AND tmp_b.cnt >= 10 AND tmp_a.author = tmp_b.author;