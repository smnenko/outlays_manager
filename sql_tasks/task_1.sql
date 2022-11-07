SELECT b.title, COUNT(n.id)
FROM notebooks_brand as b
INNER JOIN notebooks_notebook as n ON n.brand_id = b.id
GROUP BY b.title
ORDER BY count DESC;