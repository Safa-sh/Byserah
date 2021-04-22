Use Basyrah;
create DATABASE basyrah;
CREATE TABLE `patient` (
  `patient_id` varchar(10) NOT NULL,
  `total_checkup` int DEFAULT '0',
  PRIMARY KEY (`patient_id`),
  UNIQUE KEY `patient_id_UNIQUE` (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `checkup` (
  `checkup_id` int NOT NULL AUTO_INCREMENT,
  `patientID` varchar(10) NOT NULL,
  `checkup_result` varchar(100) NOT NULL,
  PRIMARY KEY (`checkup_id`),
  UNIQUE KEY `checkup_id_UNIQUE` (`checkup_id`),
  KEY `paientID_idx` (`patientID`),
  CONSTRAINT `patientID` FOREIGN KEY (`patientID`) REFERENCES `patient` (`patient_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;