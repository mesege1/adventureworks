SELECT
    DATE_TRUNC('month', OrderDate) AS OrderMonth,
    COUNT(*) AS ShippedOrdersCount,
    SUM(SubTotal) AS MonthlySubtotal
FROM
    sales.SalesOrderHeader
GROUP BY
    DATE_TRUNC('year', OrderDate),
    DATE_TRUNC('month', OrderDate)
ORDER BY
    DATE_TRUNC('year', OrderDate),
    DATE_TRUNC('month', OrderDate);
