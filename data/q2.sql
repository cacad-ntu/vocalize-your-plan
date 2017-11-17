SELECT      DISTINCT upper(p.title_abbrev)
FROM        publication as p
WHERE       p.pub_class = 'inproceedings' AND 
            p.month = 7
GROUP BY    p.title_abbrev, p.year
HAVING count(p.title_abbrev) > 200;