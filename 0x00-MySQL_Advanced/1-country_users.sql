-- Create table users
-- users have attributes: name, email, id and enum of country codes
CREATE TABLE IF NOT EXISTS `users`(
    `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL
);
