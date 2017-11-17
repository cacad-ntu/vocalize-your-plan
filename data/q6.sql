SELECT author, cnt
FROM collaborators
WHERE cnt = (
    SELECT MAX(cnt)
    FROM collaborators
);
