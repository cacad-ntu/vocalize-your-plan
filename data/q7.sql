SELECT  a.author as author, count(a.author) as cnt
FROM    pub_auth a, publication b
WHERE   
    a.pub_key = b.pub_key AND
    (b.pub_class = 'inproceedings' OR b.pub_class = 'article') AND
    lower(b.title) LIKE '%data%' AND
    b.year > 2012
GROUP BY a.author
ORDER BY cnt DESC
LIMIT 10;