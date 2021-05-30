CREATE TABLE cash_flow
(
  cfid   INT      NOT NULL AUTO_INCREMENT,
  date   DATETIME NOT NULL,
  amount INT      NOT NULL,
  type   VARCHAR  NOT NULL COMMENT 'drug/salary etc..',
  PRIMARY KEY (cfid)
);

ALTER TABLE cash_flow
  ADD CONSTRAINT UQ_cfid UNIQUE (cfid);

CREATE TABLE employees
(
  employeeID INT                    NOT NULL AUTO_INCREMENT,
  name       VARCHAR(128)           NOT NULL,
  surname    VARCHAR(128)           NOT NULL,
  sex        ENUM('Male', 'Female') NOT NULL,
  phone                             NULL    ,
  position                          NULL    ,
  salary                            NULL    ,
  PRIMARY KEY (employeeID)
);

ALTER TABLE employees
  ADD CONSTRAINT UQ_employeeID UNIQUE (employeeID);

CREATE TABLE equipment
(
  eqID             NOT NULL AUTO_INCREMENT,
  eqName           NULL    ,
  status      BOOL NOT NULL COMMENT 'work or not',
  room_number      NULL    ,
  number      INT  NOT NULL,
  PRIMARY KEY (eqID)
);

ALTER TABLE equipment
  ADD CONSTRAINT UQ_eqID UNIQUE (eqID);

CREATE TABLE meds
(
  drugID       INT     NOT NULL AUTO_INCREMENT,
  name         VARCHAR NULL    ,
  in_stock             NULL    ,
  ordered              NULL    ,
  discontinued BOOL    NOT NULL,
  price                NULL    ,
  PRIMARY KEY (drugID)
);

ALTER TABLE meds
  ADD CONSTRAINT UQ_drugID UNIQUE (drugID);

CREATE TABLE meds_perscribed
(
              NOT NULL,
  drugID  INT NOT NULL,
  visitID INT NOT NULL,
  amount      NULL    
);

CREATE TABLE owners
(
  ownerID INT          NOT NULL AUTO_INCREMENT,
  name    VARCHAR(128) NOT NULL,
  surname VARCHAR(128) NOT NULL,
  phone                NOT NULL,
  mail                 NULL    ,
  PRIMARY KEY (ownerID)
);

ALTER TABLE owners
  ADD CONSTRAINT UQ_ownerID UNIQUE (ownerID);

CREATE TABLE pets
(
  petID     INT                    NOT NULL AUTO_INCREMENT,
  ownerID   INT                    NOT NULL,
  Sex       ENUM('Male', 'Female') NULL    ,
  type      VARCHAR                NULL    ,
  birthdate DATE                   NULL    ,
  weight    DECIMAL(5,2)           NULL     COMMENT 'in kg',
  height    INT                    NULL     COMMENT 'in cm',
  PRIMARY KEY (petID)
);

ALTER TABLE pets
  ADD CONSTRAINT UQ_petID UNIQUE (petID);

CREATE TABLE rooms
(
  number INT NOT NULL,
  PRIMARY KEY (number)
);

ALTER TABLE rooms
  ADD CONSTRAINT UQ_number UNIQUE (number);

CREATE TABLE visits
(
  visitID           INT      NOT NULL AUTO_INCREMENT,
  petID             INT      NOT NULL,
  emplyeeID         INT      NOT NULL,
  registration_date DATETIME NOT NULL,
  planned_date      DATETIME NOT NULL COMMENT 'termin zaplanowany',
  real_date         DATETIME NULL     COMMENT 'kiedy wykonana',
  status            BOOL     NOT NULL COMMENT 'czy wykonana',
  cost              DECIMAL  NOT NULL COMMENT 'koszt wizyty ',
  number            INT      NOT NULL,
  PRIMARY KEY (visitID)
);

ALTER TABLE visits
  ADD CONSTRAINT UQ_visitID UNIQUE (visitID);

ALTER TABLE pets
  ADD CONSTRAINT FK_owners_TO_pets
    FOREIGN KEY (ownerID)
    REFERENCES owners (ownerID);

ALTER TABLE visits
  ADD CONSTRAINT FK_pets_TO_visits
    FOREIGN KEY (petID)
    REFERENCES pets (petID);

ALTER TABLE visits
  ADD CONSTRAINT FK_employees_TO_visits
    FOREIGN KEY (emplyeeID)
    REFERENCES employees (employeeID);

ALTER TABLE meds_perscribed
  ADD CONSTRAINT FK_meds_TO_meds_perscribed
    FOREIGN KEY (drugID)
    REFERENCES meds (drugID);

ALTER TABLE meds_perscribed
  ADD CONSTRAINT FK_visits_TO_meds_perscribed
    FOREIGN KEY (visitID)
    REFERENCES visits (visitID);

ALTER TABLE visits
  ADD CONSTRAINT FK_rooms_TO_visits
    FOREIGN KEY (number)
    REFERENCES rooms (number);

ALTER TABLE equipment
  ADD CONSTRAINT FK_rooms_TO_equipment
    FOREIGN KEY (number)
    REFERENCES rooms (number);

        
      