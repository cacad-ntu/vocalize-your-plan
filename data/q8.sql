SELECT upper(a.title_abbrev), a.title 
FROM publication a,
    (SELECT a.pub_key, count(a.pub_key) as cnt 
    FROM publication a, proceedings b, inproceedings c
    WHERE 
        a.pub_class = 'proceedings' AND 
        a.month = 6 AND
        a.pub_key = b.pub_key AND
        b.booktitle = c.booktitle
    GROUP BY a.pub_key, a.year) as tmp
WHERE tmp.cnt > 100 AND tmp.pub_key = a.pub_key;