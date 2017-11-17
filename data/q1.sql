SELECT      pub_class, COUNT(*) AS Total
FROM        publication 
WHERE       year < 2018 AND year > 1999
GROUP BY    pub_class;