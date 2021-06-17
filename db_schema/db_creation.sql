SET FOREIGN_KEY_CHECKS = 0;
CREATE OR replace SCHEMA vet_clinic;

USE vet_clinic;

CREATE TABLE `cash_flow`
(
    `cfid`   INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `date`   DATETIME     NOT NULL,
    `amount` INT          NOT NULL,
    `type`   VARCHAR(128) NOT NULL
);

CREATE TABLE `employees`
(
    `employeeID` INT UNIQUE PRIMARY KEY  NOT NULL AUTO_INCREMENT,
    `name`       VARCHAR(128)            NOT NULL,
    `surname`    VARCHAR(128)            NOT NULL,
    `sex`        ENUM ('Male', 'Female') NOT NULL,
    `phone`      varchar(128)            NULL,
    `position`   varchar(128)            NULL,
    `salary`     decimal(10, 2)          NULL
);

CREATE TABLE `equipment`
(
    `eqID`        int UNIQUE PRIMARY KEY AUTO_INCREMENT,
    `eqName`      varchar(128) NULL,
    `status`      BOOL         NOT NULL,
    `room_number` int          NULL,
    `quantity`      INT          NOT NULL
);

CREATE TABLE `meds`
(
    `drugID`       INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `name`         VARCHAR(128),
    `in_stock`     float                  NULL,
    `ordered`      float                  NULL,
    `discontinued` BOOL                   NOT NULL,
    `price`        float                  NULL
);

CREATE TABLE `meds_prescribed`
(
    `drugID`  INT   NOT NULL,
    `visitID` INT   NOT NULL,
    `amount`  float NOT NULL
);

CREATE TABLE `owners`
(
    `ownerID` INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `name`    VARCHAR(128)           NOT NULL,
    `surname` VARCHAR(128)           NOT NULL,
    `phone`   varchar(128)           NOT NULL,
    `mail`    varchar(128)           NULL
);

CREATE TABLE `pets`
(
    `petID`     INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `ownerID`   INT                    NOT NULL,
    `Sex`       ENUM ('Male', 'Female'),
    `type`      VARCHAR(128),
    `birthdate` DATE,
    `weight`    DECIMAL(5, 2),
    `height`    INT
);

CREATE TABLE `rooms`
(
    `number` INT UNIQUE PRIMARY KEY NOT NULL,
    `name`   varchar(20)
);

CREATE TABLE `visits`
(
    `visitID`           INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `petID`             INT                    NOT NULL,
    `employeeID`        INT                    NOT NULL,
    `registration_date` DATETIME               NOT NULL,
    `planned_date`      DATETIME               NOT NULL,
    `real_date`         DATETIME,
    `status`            BOOL                   NOT NULL,
    `cost`              DECIMAL(8, 2)          NOT NULL,
    `number`            INT                    NOT NULL
);

ALTER TABLE `pets`
    ADD FOREIGN KEY (`ownerID`) REFERENCES `owners` (`ownerID`);

ALTER TABLE `visits`
    ADD FOREIGN KEY (`petID`) REFERENCES `pets` (`petID`);

ALTER TABLE `visits`
    ADD FOREIGN KEY (`employeeID`) REFERENCES `employees` (`employeeID`);

ALTER TABLE `meds_prescribed`
    ADD FOREIGN KEY (`drugID`) REFERENCES `meds` (`drugID`);

ALTER TABLE `meds_prescribed`
    ADD FOREIGN KEY (`visitID`) REFERENCES `visits` (`visitID`);

ALTER TABLE `visits`
    ADD FOREIGN KEY (`number`) REFERENCES `rooms` (`number`);

ALTER TABLE `equipment`
    ADD FOREIGN KEY (`room_number`) REFERENCES `rooms` (`number`);

SET FOREIGN_KEY_CHECKS = 1;