# Customers Who Never Order

## Problem Statement

Given the following database schema:

### Table: Customers

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |

- `id` is the primary key for this table.
- Each row represents a customer with a unique ID and name.

### Table: Orders

| Column Name | Type |
|-------------|------|
| id          | int  |
| customerId  | int  |

- `id` is the primary key for this table.
- `customerId` is a foreign key referencing the `id` column in the `Customers` table.
- Each row represents an order placed by a customer.


