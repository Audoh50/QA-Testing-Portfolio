# SQL Database Testing Project

## Project Overview

This project demonstrates the use of SQL queries for database validation and software quality assurance testing.

The objective is to verify that customer, order, and product information stored in an e-commerce database is accurate, complete, and consistent with expected application behavior.

## Skills Demonstrated

- Database Validation
- SQL SELECT Statements
- WHERE Clauses
- ORDER BY
- COUNT
- JOIN Operations
- NULL Validation
- Duplicate Record Detection
- Data Integrity Testing

---

## Sample Database Tables

For this project, assume an e-commerce application contains the following tables:

- customers
- orders
- products

---

## Test 1 – Retrieve All Customers

### Test Objective

Verify that customer records can be retrieved successfully from the database.

### SQL Query

```sql
SELECT *
FROM customers;

Expected Result
The query should return all customer records stored in the customers table.

Test 2 – Find a Customer by Email Address
Test Objective
Verify that a specific registered customer exists in the database.
SQL Query

SELECT *
FROM customers
WHERE email = 'customer@example.com';

Expected Result
The database should return the customer associated with the specified email address.
Test 3 – Verify Active Orders
Test Objective
Verify orders that currently have a Pending status.
SQL Query

SELECT *
FROM orders
WHERE status = 'Pending';

Expected Result
Only orders with a Pending status should be returned.
Test 4 – Count Customer Orders
Test Objective
Verify the number of orders associated with each customer.
SQL Query

SELECT customer_id, COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id;
Expected Result
The query should return each customer ID and the total number of orders associated with that customer.

Test 5 – Validate Customer and Order Information
Test Objective
Verify that orders are correctly associated with registered customers.
SQL Query

SELECT customers.customer_id,
       customers.first_name,
       customers.last_name,
       orders.order_id,
       orders.status
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;

Expected Result
Each order should be associated with the correct customer information.

Test 6 – Check for Missing Email Addresses
Test Objective
Identify customer records containing missing email addresses.
SQL Query
SELECT *
FROM customers
WHERE email IS NULL;

Expected Result
No active customer account should contain a NULL email address if email is a required registration field.
Test 7 – Detect Duplicate Email Addresses
Test Objective
Identify duplicate customer email addresses.
SQL Query
SELECT email, COUNT(*) AS duplicate_count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;
Expected Result
The query should return no records if every customer email address is required to be unique.
Test 8 – Find Products That Are Out of Stock
Test Objective
Verify products with zero inventory.
SQL Query
SELECT product_id, product_name, stock_quantity
FROM products
WHERE stock_quantity = 0;
Expected Result
The query should return all products that are currently out of stock.
Test 9 – Sort Products by Price
Test Objective
Verify product pricing data and identify the most expensive products.
SQL Query
SELECT product_id, product_name, price
FROM products
ORDER BY price DESC;
Expected Result
Products should be returned from the highest price to the lowest price.












