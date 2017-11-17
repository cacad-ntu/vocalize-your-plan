SELECT tmp.author
FROM author a, (
    SELECT b.author as author, count(a.year) as cnt
    FROM publication a, pub_auth b, author c 
    WHERE 
        a.pub_key = b.pub_key AND
        b.author = c.name AND
        a.year > 1987
    GROUP BY b.author, a.year
) as tmp
WHERE 
    tmp.author = a.name AND
    lower(a.last_name) like 'h%' 
GROUP BY tmp.author
HAVING count(tmp.author) >= 30;