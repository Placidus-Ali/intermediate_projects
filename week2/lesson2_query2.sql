-- SQLite

/* Write a query for paid courses, showing the course with the 
highest sales per month */
SELECT course_id, num_reviews
FROM udemy_courses
WHERE is_paid = TRUE AND num_reviews != 0 
ORDER BY num_reviews DESC; 