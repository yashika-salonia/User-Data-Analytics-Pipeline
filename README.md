# 🚀 Mini Data Pipeline for User Activity Analysis

## 📌 Overview

This project demonstrates a modular **data engineering pipeline** that processes and analyzes raw user activity data using Python and SQLite. It simulates real-world ETL workflows by transforming raw CSV data into structured insights and storing it in a database for analysis.

## ⚙️ Tech Stack

* Python
* Pandas
* SQLite (SQL)
* Matplotlib
* CSV
* Git & GitHub

## 🔄 Pipeline Workflow

### 1. Data Extraction

* Raw user activity data is loaded from CSV files
* Dataset includes session time, subject, and distraction metrics

### 2. Data Transformation

* Data cleaning and preprocessing applied
* Feature engineering performed to calculate:

  **Focus Score = Session Time − (Distraction Count × 5)**

### 3. Data Loading

* Processed data stored in **SQLite database**
* Structured storage enables SQL-based querying and analysis

### 4. Data Analysis

* SQL queries used to extract insights from processed data
* Visualizations generated to understand productivity trends

## 📊 Key Insights

* Higher distraction counts negatively impact focus score
* Subject-wise analysis reveals variation in productivity levels
* Session time correlates with improved performance when distractions are low

## 📁 Project Structure

```
data-pipeline-user-analytics/
│
├── data/
│   └── raw_data.csv
│
├── database/
│   └── analytics.db
│
├── scripts/
│   ├── ingest_to_sql.py
│   ├── query_analysis.py
│   ├── transform.py
│   ├── visualize.py
│
├── output/
│   └── charts/
│
├── main.py
├── requirements.txt
└── README.md
```

## ▶️ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run full pipeline
python main.py
```

## 📈 Visualizations

The project generates the following charts:

* Average session time per subject
* Relationship between distractions and productivity

## 🚀 Future Improvements

* Replace SQLite with PostgreSQL for scalable storage
* Automate pipeline using Apache Airflow
* Add real-time data ingestion support
* Deploy as a cloud-based analytics system

## 🧠 Key Learnings

* ETL pipeline design and implementation
* SQL-based data querying and storage
* Feature engineering for behavioral analytics
* Data visualization and insight generation
* Modular software design for scalability

#### made with curosity - Yashika ;) 
