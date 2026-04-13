# 🚕 NYC Taxi Data Engineering Pipeline (Databricks + PySpark)

## 📌 Overview

This project implements a fully automated **end-to-end data engineering pipeline** for NYC Yellow Taxi data using **Databricks, PySpark, Delta Lake, and Azure Data Lake Storage (ADLS Gen2)**.

The pipeline follows the **Medallion Architecture**:

```text
Landing → Bronze → Silver → Gold → Export
```

It ingests monthly datasets, processes and enriches data, applies SCD Type 2 logic, and produces analytics-ready outputs.

---

## 🏗️ Architecture

```text
📅 Databricks Scheduled Job
        ↓
📥 Landing (Raw Files)
        ↓
🧱 Bronze (Raw Tables)
        ↓
🧹 Silver (Cleansed + Enriched)
        ↓
📊 Gold (Aggregated Metrics)
        ↓
📤 Export (External JSON)
```

---

## ⚙️ Key Features

* ⏰ **Automated monthly ingestion** using Databricks Jobs
* 📥 Dynamic data download from NYC Taxi public dataset
* 🔄 **Idempotent pipeline** (prevents duplicate ingestion)
* 🧹 Data cleansing and transformation using PySpark
* 🧠 Feature engineering (trip duration, decoded fields)
* 🗂️ **SCD Type 2 implementation** for dimension tables
* 🔗 Data enrichment via joins (pickup & dropoff zones)
* 📊 Aggregated analytics for reporting (Gold layer)
* 📤 Export to external storage (JSON format)
* 📈 End-to-end data validation (EDA across layers)

---

## 📂 Project Structure

```text
modules/
│
├── data_loader/
│   └── file_downloader.py
│
├── utils/
│   └── date_utils.py
│
notebooks/
│
├── ingestion/
├── transformation/
├── silver/
├── gold/
├── export/
├── eda/
```

---

## 🧱 Data Layers

### 🔹 Landing Layer

* Raw files downloaded from source
* Stored in:

```text
/Volumes/nyctaxi/00_landing/
```

---

### 🔹 Bronze Layer

* Raw data loaded into Delta tables
* Minimal transformation
* Example:

```text
nyctaxi.01_bronze.yellow_trips_raw
```

---

### 🔹 Silver Layer

#### ✅ Cleansed Trips

* Standardized schema
* Derived columns:

  * `trip_duration`
  * decoded fields (`vendor`, `rate_type`, `payment_type`)

#### ✅ Taxi Zone Lookup (SCD Type 2)

* Tracks historical changes using:

  * `effective_date`
  * `end_date`

#### ✅ Enriched Trips

* Joins trip data with lookup table
* Adds:

  * pickup/dropoff borough
  * pickup/dropoff zone

---

### 🔹 Gold Layer

**Table:** `nyctaxi.03_gold.daily_trip_summary`

Aggregated metrics:

* total trips
* average passengers
* average distance
* average fare
* min/max fare
* total revenue

Grouped by:

```text
pickup_date
```

---

### 🔹 Export Layer

* Format: JSON
* Partitioned by:

  * `vendor`
  * `year_month`

Stored in ADLS Gen2:

```text
abfss://nyctaxi-yellow@<storage-account>.dfs.core.windows.net/yellow_trips_export/
```

---

## 🔁 Pipeline Flow

1. **Ingestion**

   * Scheduled Databricks job downloads monthly data
   * Stores files in landing layer

2. **Bronze**

   * Raw data loaded into Delta tables

3. **Silver**

   * Data cleaned and transformed
   * Lookup table maintained with SCD Type 2
   * Trips enriched with zone data

4. **Gold**

   * Daily aggregations computed

5. **Export**

   * Data written to external storage in JSON format

---

## ⏰ Automated Ingestion

* Monthly scheduled job in Databricks
* Downloads data from:

  * NYC Taxi & Limousine Commission (TLC)
* Checks if file exists before downloading
* Uses `dbutils.jobs.taskValues` to control downstream execution

---

## 📊 Data Validation (EDA)

EDA is performed across all layers to ensure data integrity:

### ✔️ Checks performed:

* Record count consistency (Bronze → Silver → Gold → Export)
* Join validation (no data loss or duplication)
* Aggregation validation
* SCD Type 2 table inspection
* Export completeness verification

---

## 🧠 Key Concepts Used

* Medallion Architecture
* Delta Lake (ACID transactions)
* Slowly Changing Dimension (SCD Type 2)
* Incremental processing
* Idempotent pipeline design
* Data enrichment via joins
* Partitioned data storage

---

## 🛠️ Technologies

* Databricks
* PySpark
* Delta Lake
* Unity Catalog
* Azure Data Lake Storage (ADLS Gen2)

---

## ⚠️ Future Improvements

* Optimize SCD Type 2 merge logic (single-pass merge)
* Replace hardcoded mappings with lookup tables
* Add data quality checks (nulls, duplicates)
* Implement retry logic for ingestion
* Add monitoring & alerting
* Parameterize pipelines

---

## 🚀 How to Run

1. Execute ingestion notebook (downloads data)
2. Run Bronze load
3. Run Silver transformations
4. Run enrichment pipeline
5. Run Gold aggregation
6. Run export job
7. Validate using EDA notebook

---

## 📈 Sample Output

| pickup_date | total_trips | average_passengers | total_revenue |
| ----------- | ----------- | ------------------ | ------------- |
| 2026-02-01  | 120,000     | 1.3                | 2,300,000     |



