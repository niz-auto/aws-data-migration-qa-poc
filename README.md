![CI](https://github.com/niz-auto/aws-data-migration-qa-poc/actions/workflows/tests.yml/badge.svg)
# AWS Data Migration QA Automation POC

This repository demonstrates a **QA automation framework for validating On-Prem → AWS data migration pipelines**.

Example scenario:
Two legacy systems containing **members list and dues data** are migrated to AWS.


Pipeline architecture:

On-Prem System
↓
CSV Export (Source)  
↓  
AWS S3 Landing Zone  
↓  
AWS ETL Pipeline (Glue / Databricks)  
↓  
AWS RDS  
↓  
Vendor Update via API  
↓  
Vendor Data Warehouse

---

## Validation Strategy

The framework validates data at each layer:

1. CSV source validation
2. ETL Validation
3. AWS RDS database validation
4. Vendor API validation
5. UI report validation

---

## Technologies Used

- Python
- Playwright
- Pandas
- AWS RDS validation scripts
- CI/CD pipelines
- QA dashboards
- Jira & XRay (addon)
---

## Test Types

| Test Type | Description |
|------|------|
CSV validation | schema, duplicates, null checks |
Data reconciliation | source vs RDS |
API validation | vendor endpoints |
UI validation | business dashboards |

---

## Monitoring and Alerts

Pipeline monitoring is simulated using:

- CloudWatch logs
- validation scripts
- automated alerts

---

## Running Tests

Install dependencies:
