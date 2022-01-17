-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: data_source
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `os`
--

DROP TABLE IF EXISTS `os`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `os` (
  `channel_id` bigint unsigned NOT NULL,
  `channel_name` varchar(255) DEFAULT NULL,
  `channel_details` varchar(255) DEFAULT NULL,
  `staff_id` bigint unsigned NOT NULL,
  `staff_name` varchar(255) DEFAULT NULL,
  `staff_details` varchar(255) DEFAULT NULL,
  `artefact_id` bigint unsigned NOT NULL,
  `artefact_name` varchar(255) DEFAULT NULL,
  `artefact_details` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`channel_id`),
  UNIQUE KEY `channel_id` (`channel_id`),
  UNIQUE KEY `staff_id` (`staff_id`),
  UNIQUE KEY `artefact_id` (`artefact_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `os`
--

LOCK TABLES `os` WRITE;
/*!40000 ALTER TABLE `os` DISABLE KEYS */;
/*!40000 ALTER TABLE `os` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `processes`
--

DROP TABLE IF EXISTS `processes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `processes` (
  `event_sequence_id` bigint unsigned NOT NULL,
  `next_event_sequence_id` bigint unsigned DEFAULT NULL,
  `event_code` char(20) DEFAULT NULL,
  `event_time` datetime DEFAULT NULL,
  `event_details` varchar(255) DEFAULT NULL,
  `event_source_file` text,
  `event_source_variables` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`event_sequence_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `processes`
--

LOCK TABLES `processes` WRITE;
/*!40000 ALTER TABLE `processes` DISABLE KEYS */;
/*!40000 ALTER TABLE `processes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sys`
--

DROP TABLE IF EXISTS `sys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sys` (
  `platform_id` bigint NOT NULL,
  `platform_name` varchar(255) DEFAULT NULL,
  `platform_details` varchar(255) DEFAULT NULL,
  `acces_variables` varchar(255) DEFAULT NULL,
  `customer_name` varchar(255) DEFAULT NULL,
  `customer_id` bigint unsigned NOT NULL,
  `title` char(20) DEFAULT NULL,
  `gender` char(3) DEFAULT NULL,
  `customer_details` varchar(255) DEFAULT NULL,
  `supplier_id` bigint unsigned NOT NULL,
  `supplier_name` varchar(255) DEFAULT NULL,
  `supplier_details` varchar(255) DEFAULT NULL,
  `service_code` bigint NOT NULL,
  `service_name` varchar(255) DEFAULT NULL,
  `services_details` varchar(255) DEFAULT NULL,
  `location_id` bigint unsigned NOT NULL,
  `location_name` varchar(255) DEFAULT NULL,
  `location_details` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`service_code`),
  UNIQUE KEY `customer_id` (`customer_id`),
  UNIQUE KEY `supplier_id` (`supplier_id`),
  UNIQUE KEY `service_code` (`service_code`),
  UNIQUE KEY `location_id` (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sys`
--

LOCK TABLES `sys` WRITE;
/*!40000 ALTER TABLE `sys` DISABLE KEYS */;
INSERT INTO `sys` VALUES (64564,'gdfg','gdfgd','gdfg','gdfgd',42345,'gdfg','f','gdfg',4242,'fsdfsf','fsdfsdfsd',4234,'fafaf','fasfasf',4124,'fsdaf','fsadfsadf'),(4234,'dfsdfs','fsdfsd','fsdfsfs','fsdfs',4234,'fsdfsd','f','fsdfsdfsd',4532,'fsdfds','fsdffs',4325,'fsdfsdfa','dasfsafasfsa',4234,'sdfsdf','fsdffsdfsd'),(645,'gfdgdf','gdfg','gdfgd','gdfggdfgf',2342,'gdfgd','f','gdfgg',44756,'fsdfsdf','fsdfsdfs',8768,'sadas','fasfasf',41242,'dasdas','dasdsa');
/*!40000 ALTER TABLE `sys` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-17 12:56:19