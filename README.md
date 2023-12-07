# Streaming Data Pipeline with AWS Glue

![AWS Glue To Athena](GlueAthena.png)

## Overview

This repository contains code and documentation for a streaming data pipeline built using AWS services and technologies. The pipeline efficiently captures, processes, and visualizes streaming data for robust business analytics.

## Project Steps

### 1. Real-time Data Extraction with EC2 Instance

- Implemented an EC2 instance for real-time data extraction using Python.
- Ensure the EC2 instance is set up with the necessary Python libraries and configurations.

### 2. Data Flow Optimization with Kinesis

- Optimize data flow using a Kinesis producer for efficient data capture and transfer.
- Ensure the Kinesis stream is correctly configured to handle the data volume.

### 3. Parallel Data Processing with AWS Glue and Lambda

- Orchestrate parallel data processing operations with AWS Glue.
- Utilize Lambda functions to ensure smooth and efficient execution of data tasks.
  
### 4. Automated Backup and Data Querying

- Implement automated backup with Kinesis triggers and Lambda functions.
- Enhance data availability and reliability.
- Enable streamlined data querying using Athena.
  
### 5. End-to-End Data Processing with AWS Glue and Spark

- Leverage AWS Glue and Apache Spark for end-to-end data processing.
- Includes extraction, cleansing, processing, transformation, and storage of data.
  
### 6. Business Analytics and Visualization

- Utilize Amazon Redshift for data warehousing.
- Enable high-performance querying and analytics on large datasets.
- Create interactive dashboards and reports for business analytics using Amazon QuickSight.

## Project Structure

- `/code`: Contains Python scripts and AWS Glue jobs for data processing.
- `/documentation`: Includes setup and usage documentation.
