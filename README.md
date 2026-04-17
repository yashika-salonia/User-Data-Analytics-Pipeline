# 🚀 Mini Data Pipeline for User Activity Analysis

## 📌 Overview

This project demonstrates a simplified **ETL (Extract, Transform, Load) data pipeline** built using Python. It processes raw user activity data and generates meaningful insights through data transformation and visualization.

The pipeline simulates real-world data engineering workflows on a smaller scale using CSV-based data.

---

## ⚙️ Tech Stack

* Python
* Pandas
* Matplotlib
* CSV (as data source)
* Git & GitHub

---

## 🔄 Pipeline Workflow

### 1. Extract

* Raw user activity data is loaded from a CSV file
* Data includes session time, subject, and distraction metrics

### 2. Transform

* Feature engineering is applied:

  **Focus Score = Session Time − (Distraction Count × 5)**

* Invalid or low-quality data is filtered out

### 3. Load

* Cleaned and processed data is stored in a new CSV file
* Ready for further analysis or integration

### 4. Analyze

* Data visualization is performed to extract insights:

  * Subject-wise focus trends
  * Impact of distractions on productivity

---

## 📊 Visual Insights

### 1. Average Focus Score per Subject

* Helps identify which subjects require more concentration

### 2. Distraction vs Focus Score

* Shows negative correlation between distractions and productivity

---

## 📁 Project Structure

```
data-pipeline-user-analytics/
│
├── data/
│   └── raw_data.csv
│
├── scripts/
│   ├── ingest.py
│   ├── transform.py
│   ├── load.py
│   ├── analyze.py
│   └── generate_data.py
│
├── output/
│   ├── processed_data.csv
│   └── charts/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Generate dataset
python scripts/generate_data.py

# Run pipeline
python main.py
```

---

## 📈 Sample Insights

* Users with higher distraction counts tend to have significantly lower focus scores
* Some subjects (like DSA) show higher variability in focus

---

## 🚀 Future Improvements

* Replace CSV with PostgreSQL for structured storage
* Scale processing using PySpark for large datasets
* Automate pipeline using Airflow
* Deploy as a cloud-based data pipeline (AWS/GCP)

---

## 🧠 Key Learnings

* Understanding of ETL pipeline design
* Data transformation and feature engineering
* Basic data analysis and visualization
* Structuring real-world data projects

---

## 📬 Author
Made with curosity - Yashika ;)
