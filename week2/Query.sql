-- SQLite

/*Write a query for paid courses, showing the course with the
highest number of subscribers per month */
SELECT course_id, num_subscribers
FROM udemy_courses
WHERE is_paid = TRUE AND num_subscribers != 0
ORDER BY num_subscribers DESC;

