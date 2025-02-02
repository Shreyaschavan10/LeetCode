# Find Low Fat and Recyclable Products

## Table: Products

The `Products` table consists of the following columns:

- `product_id` (int) - The unique identifier for each product.
- `low_fats` (ENUM 'Y', 'N') - Indicates whether the product is low fat ('Y' for Yes, 'N' for No).
- `recyclable` (ENUM 'Y', 'N') - Indicates whether the product is recyclable ('Y' for Yes, 'N' for No).

## Problem Statement

Write an SQL query and pandas script to find the `product_id` of products that are **both** low fat and recyclable.

## Example

### Input:
```
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
