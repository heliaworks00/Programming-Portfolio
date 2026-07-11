CREATE TABLE customers 
(
  customerID INT PRIMARY KEY,
  customerName NVARCHAR(100),
  City NVARCHAR(50),
  Age INT
);

INSERT INTO Customers
VALUES
(1, N'هلیا احمدی', N'تهران', 18),
(2, N'علی رضایی', N'اصفهان', 25),
(3, N'سارا محمدی', N'شیراز', 22),
(4, N'حامد باغی', N'رشت', 30);

CREATE TABLE Orders
(
  OrderID INT PRIMARY KEY,
  CustomerID INT,
  ProductName NVARCHAR(100),
  Price DECIMAL(10,2),
  OrderDate DATE,
  
  FOREIGN KEY (CustomerID)
  REFERENCES Customers(CustomerID)
);

INSERT INTO Orders
VALUES
(101, 1, N'لپ تاپ', 45000000, '2025-08-01'),
(102, 1, N'ماوس', 800000, '2025-08-05'),
(103, 2, N'کیبورد', 1500000, '2025-08-07'),
(104, 3, N'مانیتور', 12000000, '2025-08-10');

SELECT
c.CustomerName,
COUNT(o.OrderID) AS NumberOfOrders,
AVG(o.Price) AS AverageOrderPrice,
MAX(o.Price) AS MostExpensiveOrder
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName, c.CustomerID;
