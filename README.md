## 📊 Exploratory Data Analysis (EDA) & Validation

To ensure data quality and pipeline integrity, EDA checks were performed across all layers of the Medallion Architecture.

### 🔍 Validation Strategy

Record counts were analyzed at each stage:

* **Bronze:** Raw ingested data
* **Silver (Cleansed):** After data cleaning and transformations
* **Silver (Enriched):** After joining with lookup tables
* **Gold:** Aggregated daily metrics
* **Export:** Final exported dataset

### 📈 Key Checks

* Monthly record counts consistency across layers
* Validation of joins (no data loss or duplication)
* Aggregation accuracy in Gold layer
* Verification of exported data completeness
* Inspection of SCD Type 2 dimension table (`taxi_zone_lookup`)

### 🧠 Outcome

This analysis ensures:

* Data integrity throughout the pipeline
* Accurate transformations and aggregations
* Reliable outputs for downstream analytics and reporting
