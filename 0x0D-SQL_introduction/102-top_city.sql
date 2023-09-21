-- List the first 3 cities
-- cat 102-top_city.sql | mysql -hlocalhost -uroot -p
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
