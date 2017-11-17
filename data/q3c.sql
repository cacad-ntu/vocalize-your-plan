SELECT tmp.author
FROM 
    (SELECT b.author, count(b.author) as pub_cnt
    FROM publication as a, pub_auth as b
    WHERE a.pub_key = b.pub_key AND year = 2015 AND pub_type = 'conf' AND title_abbrev = 'wasa'
    GROUP BY b.author) AS tmp
WHERE tmp.pub_cnt > 1;