-- list avergae temperaturesi
-- cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
