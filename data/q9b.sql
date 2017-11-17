SELECT b.author, count(b.author)
FROM publication a, pub_auth b
WHERE year IN (
    SELECT min(year) FROM publication
) AND a.pub_key = b.pub_key
GROUP BY b.author;
