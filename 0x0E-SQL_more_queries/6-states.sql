-- create databse hbtn_0d_usa and table states.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (`id` NOT NULL AUTO_INCREMENT PRIMARY KEY (`id`) UNIQUE, `name` NOT NULL VARCHAR(256)); 
