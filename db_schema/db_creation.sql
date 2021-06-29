SET FOREIGN_KEY_CHECKS = 0;
CREATE OR replace SCHEMA vet_clinic;

USE vet_clinic;

CREATE TABLE `cash_flow` (
  `cfid` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  `amount` INT NOT NULL,
  `type` VARCHAR(128) NOT NULL
);

CREATE TABLE `employees` (
  `employeeID` INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128) NOT NULL,
  `surname` VARCHAR(128) NOT NULL,
  `sex` ENUM ('Male', 'Female') NOT NULL,
  `phone` varchar(128),
  `position` varchar(128),
  `salary` decimal(10,2)
);

CREATE TABLE `equipment` (
  `eqID` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `eqName` varchar(128),
  `status` BOOL NOT NULL,
  `roomID` int,
  `quantity` INT NOT NULL
);

CREATE TABLE `meds` (
  `drugID` INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128),
  `in_stock` int,
  `ordered` int,
  `discontinued` BOOL NOT NULL,
  `price` decimal(8,2)
);

CREATE TABLE `meds_prescribed` (
  `drugID` INT NOT NULL,
  `visitID` INT NOT NULL,
  `amount` float NOT NULL
);

CREATE TABLE `owners` (
  `ownerID` INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128) NOT NULL,
  `surname` VARCHAR(128) NOT NULL,
  `phone` varchar(128) NOT NULL,
  `mail` varchar(128)
);

CREATE TABLE `pets` (
  `petID` INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `ownerID` INT NOT NULL,
  `Sex` ENUM ('Male', 'Female'),
  `type` VARCHAR(128),
  `birthdate` DATE,
  `weight` DECIMAL(5,2),
  `height` DECIMAL(10,3)
);

CREATE TABLE `rooms` (
  `roomID` INT UNIQUE PRIMARY KEY NOT NULL,
  `number` INT,
  `name` varchar(20)
);

CREATE TABLE `visits` (
  `visitID` INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `petID` INT NOT NULL,
  `employeeID` INT NOT NULL,
  `registration_date` DATETIME NOT NULL,
  `planned_date` DATETIME NOT NULL,
  `real_date` DATETIME,
  `cost` DECIMAL(8,2) NOT NULL,
  `roomID` INT NOT NULL
);

ALTER TABLE `pets` ADD FOREIGN KEY (`ownerID`) REFERENCES `owners` (`ownerID`);

ALTER TABLE `visits` ADD FOREIGN KEY (`petID`) REFERENCES `pets` (`petID`);

ALTER TABLE `visits` ADD FOREIGN KEY (`employeeID`) REFERENCES `employees` (`employeeID`);

ALTER TABLE `meds_prescribed` ADD FOREIGN KEY (`drugID`) REFERENCES `meds` (`drugID`);

ALTER TABLE `meds_prescribed` ADD FOREIGN KEY (`visitID`) REFERENCES `visits` (`visitID`);

ALTER TABLE `visits` ADD FOREIGN KEY (`roomID`) REFERENCES `rooms` (`roomID`);

ALTER TABLE `equipment` ADD FOREIGN KEY (`roomID`) REFERENCES `rooms` (`roomID`);

SET FOREIGN_KEY_CHECKS = 1;

CREATE TRIGGER koszty
    AFTER INSERT
    ON visits
    FOR EACH ROW
    INSERT INTO cash_flow (date, amount, type)
    VALUES (new.planned_date, NEW.cost, 'wizyta');

SET GLOBAL event_scheduler = ON;

CREATE EVENT IF NOT EXISTS wyplaty
ON SCHEDULE EVERY 1 MONTH
STARTS DATE("2020-01-01")
DO
INSERT INTO vet_clinic.cash_flow(date, amount, type) SELECT  CURDATE(), salary, 'WYPLATA' FROM employees