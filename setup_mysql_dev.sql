-- script SQL that prepares a MySQL server for the project AirBnB
-- A database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- A new user hbnb_dev (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';;
-- The password of hbnb_dev should be set to hbnb_dev_pwd
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail
FLUSH PRIVILEGES;
