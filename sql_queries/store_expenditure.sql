SELECT
    c.CustomerID,
    s.BusinessEntityID AS StoreID,
    s.Name AS StoreName,
    SUM(soh.SubTotal) AS TotalAmountOrdered
FROM
    SalesOrderHeader soh
JOIN
    Customer c ON soh.CustomerID = c.CustomerID
JOIN
    Store s ON c.StoreID = s.BusinessEntityID
WHERE
    soh.Status = 5 -- Shipped orders
GROUP BY
    c.CustomerID,
    s.BusinessEntityID,
    s.Name
ORDER BY
    TotalAmountOrdered DESC;