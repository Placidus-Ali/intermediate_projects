-- SQLite
USE udemy_courses.db;
SELECT course_id, course_title, 
MAX(num_subscribers),
strftime("%m-%Y", published_timestamp) as MonthYear
FROM udemy_courses
GROUP BY strftime("%m-%Y", published_timestamp);