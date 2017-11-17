SELECT a.author
FROM pub_auth a JOIN publication b
ON 
    a.pub_key = b.pub_key
WHERE
    b.year = 2017
GROUP BY a.author
HAVING count(a.author) > 20;