-- SQLite

/*Write a query for paid courses, showing the course with the
highest number of subscribers per month */

SELECT course_id, course_title, 
MAX(num_subscribers),
strftime("%Y-%m", published_timestamp) as YearMonth
FROM udemy_courses
GROUP BY strftime("%Y-%m", published_timestamp)
