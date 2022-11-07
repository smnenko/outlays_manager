SELECT
	CEIL(width / 5) * 5 as width,
	CEIL(height / 5) * 5 as height,
	CEIL(depth / 5) * 5 as depth,
	COUNT(*)
FROM notebooks_notebook
GROUP BY width, height, depth
ORDER BY width, height, depth;