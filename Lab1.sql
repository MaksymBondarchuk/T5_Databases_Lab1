SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


-- -----------------------------------------------------
-- Table `E_Transactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `E_Transactions` (
  `Transaction_ID` INT NOT NULL,
  `User_ID` INT NULL,
  `Bill_ID` INT NULL,
  `Time_ID` INT NULL,
  `Successful` TINYINT(1) NULL,
  UNIQUE INDEX `Time_ID_UNIQUE` (`Time_ID` ASC),
  UNIQUE INDEX `Bill_ID_UNIQUE` (`Bill_ID` ASC),
  UNIQUE INDEX `User_ID_UNIQUE` (`User_ID` ASC),
  UNIQUE INDEX `Transaction_ID_UNIQUE` (`Transaction_ID` ASC),
  PRIMARY KEY (`Transaction_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `D_User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `D_User` (
  `User_Id` INT NULL,
  `Name` VARCHAR(45) NULL,
  `Age` INT NULL,
  `Years_with_bank` INT NULL,
  `Comment` TEXT NULL,
  UNIQUE INDEX `User_Id_UNIQUE` (`User_Id` ASC),
  CONSTRAINT `User_ID`
    FOREIGN KEY (`User_Id`)
    REFERENCES `E_Transactions` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `D_Time`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `D_Time` (
  `Time_Id` INT NULL,
  `DateTime` DATETIME NULL,
  `In_day_time` TINYINT(1) NULL,
  UNIQUE INDEX `Time_Id_UNIQUE` (`Time_Id` ASC),
  CONSTRAINT `Time_Id`
    FOREIGN KEY (`Time_Id`)
    REFERENCES `E_Transactions` (`Time_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `D_Bill`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `D_Bill` (
  `Bill_ID` INT NULL,
  `Amount` DOUBLE NULL,
  `Average_amount_for_month` DOUBLE NULL,
  UNIQUE INDEX `Bill_ID_UNIQUE` (`Bill_ID` ASC),
  CONSTRAINT `Bill_ID`
    FOREIGN KEY (`Bill_ID`)
    REFERENCES `E_Transactions` (`Bill_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
