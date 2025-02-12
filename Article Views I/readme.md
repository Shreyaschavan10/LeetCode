# Find Authors Who Viewed Their Own Articles

## Table: Views

The `Views` table contains records of article views, where each row represents an article viewed by a user. If an author's `author_id` matches the `viewer_id`, it means the author has viewed their own article.

### Schema:
```sql
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
```
- There is no primary key, so the table may contain duplicate rows.
- If `author_id = viewer_id`, the author has viewed their own article.



🚀 **Happy Coding!** 🎯
