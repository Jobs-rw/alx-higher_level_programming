-- max value by state
-- cat 103-max_state.sql | mysql -hlocalhost -uroot -p
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
