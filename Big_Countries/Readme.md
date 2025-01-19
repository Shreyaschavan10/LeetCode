# Country Table Overview

This document provides details about the structure and contents of the `Country` table and describes its columns, data types, and the type of information it stores.

## Table Schema

| Column Name | Type    | Description                                           |
|-------------|---------|-------------------------------------------------------|
| `name`      | varchar | Name of the country (Primary Key, unique values).     |
| `continent` | varchar | Continent to which the country belongs.              |
| `area`      | int     | Area of the country in square kilometers.            |
| `population`| int     | Population of the country.                           |
| `gdp`       | bigint  | GDP (Gross Domestic Product) of the country in USD.  |

## Primary Key
- The `name` column serves as the primary key, ensuring each country's entry is unique.

## Sample Data
Below is an example of the table's data:

| Name         | Continent | Area    | Population | GDP           |
|--------------|-----------|---------|------------|---------------|
| Afghanistan  | Asia      | 652230  | 25500100   | 20343000000   |
| Albania      | Europe    | 28748   | 2831741    | 12960000000   |
| Algeria      | Africa    | 2381741 | 37100000   | 188681000000  |
| Andorra      | Europe    | 468     | 78115      | 3712000000    |
| Angola       | Africa    | 1246700 | 20609294   | 100990000000  |

## Description
Each row in the `Country` table provides detailed information about a specific country. This includes:
1. The **name** of the country.
2. The **continent** to which the country belongs (e.g., Asia, Europe).
3. The **area** of the country, measured in square kilometers.
4. The **population** of the country.
5. The **GDP** value of the country in US dollars.

## Usage
This table can be utilized for various types of queries, including but not limited to:
- Finding countries by continent.
- Comparing the GDP or population of countries.
- Analyzing population density (population/area).
- Grouping countries by continent for aggregated statistics.

## Example Query
To find the top 5 countries with the highest population:
```sql
SELECT name, population 
FROM Country
ORDER BY population DESC
LIMIT 5;
```

## Notes
- The `gdp` column uses a `bigint` type to accommodate large GDP values for countries with significant economies.
- Be cautious with computations involving the `area` and `population` columns to ensure meaningful results (e.g., calculating density).

---
