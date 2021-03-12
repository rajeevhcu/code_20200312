create database customer;

CREATE TABLE `bmi` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `gender` VARCHAR(10) NOT NULL,
    `height_cm` DOUBLE NOT NULL,
    `weight_kg` DOUBLE NOT NULL,
    `bmi` DOUBLE NOT NULL,
    `bmi_category` VARCHAR(30) NOT NULL,
    `health_risk` VARCHAR(30) NOT NULL,
    PRIMARY KEY (`id`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8;
