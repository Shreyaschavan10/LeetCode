SELECT c.name AS Customers
FROM dbo.Customers c
LEFT JOIN dbo.Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;
