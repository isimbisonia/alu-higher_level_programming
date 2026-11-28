-- Creates the database hbtn_0d_2 and the user user_0d_2 with only the SELECT privilege on it
-- Creates the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates the user with the password user_0d_2_pwd if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Gives user_0d_2 only the SELECT privilege on hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
