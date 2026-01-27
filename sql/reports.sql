-- name: revenue_by_city
SELECT
  city,
  SUM(total_price) AS total_revenue,
  COUNT(*) AS total_orders
FROM sales
GROUP BY city
ORDER BY total_revenue DESC;

-- name: top_products
SELECT
  product,
  SUM(total_price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;

-- name: category_summary
SELECT
  category,
  SUM(quantity) AS total_units_sold,
  SUM(total_price) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;

-- name: daily_sales
SELECT
  date,
  SUM(total_price) AS daily_revenue,
  COUNT(*) AS orders
FROM sales
GROUP BY date
ORDER BY date ASC;
