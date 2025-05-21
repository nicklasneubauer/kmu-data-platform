# kmu-data-platform

📊 End-to-end data platform for small businesses.

This modular project demonstrates how to ingest, transform, store, and visualize business data with automation. It includes components for data ingestion, cleaning, storage, analytics dashboards, and alerting – ideal for real-world data engineering use cases.

## 📁 Project structure

- `ingestion/` – CSV/API loaders
- `transform/` – data cleaning logic
- `db/` – database schema and models
- `dashboard/` – Streamlit or Superset configuration
- `automation/` – n8n workflows and scheduling logic
- `tests/` – unit tests for transformation logic

## ✅ Goals

- Automate ingestion of sales or marketing data
- Clean and transform data for reporting
- Store results in a central database
- Trigger alerts and visual dashboards

## 🔧 Stack

- Python (pandas, SQLAlchemy, requests)
- PostgreSQL or SQLite
- Superset / Streamlit
- n8n for automation
