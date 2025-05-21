# kmu-data-platform

📊 End-to-end data platform for small businesses.

This modular project demonstrates how to ingest, transform, store, and visualize business data with automation. It includes components for data ingestion, cleaning, storage, analytics dashboards, alerting, logging, and error monitoring – ideal for real-world data engineering use cases.

---

## 📁 Project structure

- `ingestion/` – CSV/API loaders
- `transform/` – data cleaning logic
- `db/` – database schema, import scripts, logging, and alerts
- `dashboard/` – Streamlit dashboard and admin interface
- `automation/` – n8n workflows and scheduling logic
- `tests/` – unit tests for transformation logic
- `webhook_server.py` – FastAPI Webhook endpoint for triggering imports

---

## ✅ Key Features

- Automated ingestion (CSV + API)
- Data cleaning and transformation with Pandas
- SQLAlchemy-based database layer (SQLite or PostgreSQL)
- Streamlit dashboard with customer filtering & PDF export
- Admin dashboard with manual trigger and import monitoring
- n8n automation (cron, webhook, Slack/email alert)
- Logging to `import.log`
- Email alerts on import errors via SMTP

---

## 🔧 Stack

- Python (pandas, SQLAlchemy, requests, matplotlib, fpdf)
- SQLite (default, replaceable with PostgreSQL)
- Streamlit (dashboard + admin)
- FastAPI (webhook endpoint)
- n8n (workflow automation)
- SMTP (for alerting)

---

## 🧩 Modules Overview

### Ingestion Module

Handles the import of structured data from:
- Local CSV files (e.g. sales reports)
- Public or private APIs (e.g. CRM, tools, financial data)

#### Usage
```bash
python ingestion/import_data.py
```

---

### Transform Module

Cleans and normalizes imported data.

#### Features
- Remove incomplete/malformed rows
- Convert dates and numeric values
- Normalize customer names

#### Usage
```bash
python transform/sample_transform.py
```

---

### Database Module

Defines schema and import logic.

#### Features
- ORM model for `sales` table
- One-click SQLite setup
- Automatic data import from CSV with logging + alerting

#### Usage
```bash
python db/models.py           # Setup DB
python db/import_data.py      # Import data
```

Environment variables for email alerts (via `.env` or shell):
```
ALERT_EMAIL_FROM=alerts@example.com
ALERT_EMAIL_TO=admin@example.com
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
```

---

### Dashboard Module

Streamlit UI for data visualization and PDF reporting.

#### Features
- Customer filter (dropdown)
- KPIs: total sales, records
- Charts: sales by customer, over time
- PDF export with embedded charts

#### Run
```bash
streamlit run dashboard/app.py
```

---

### Admin Dashboard

Streamlit UI for pipeline monitoring.

#### Features
- View database stats
- Trigger manual import
- Read from `import.log`

#### Run
```bash
streamlit run dashboard/admin.py
```

---

### Automation Module (n8n)

Automates data imports and notifications.

#### Example Workflow
- Trigger: Cron (daily)
- Action: Webhook call to `webhook/import-sales`
- Follow-up: Slack/email notification

#### Usage
```bash
docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
```

---

### Webhook Endpoint (FastAPI)

Trigger the import script from n8n or another service.

#### Run locally
```bash
uvicorn webhook_server:app --reload
```

#### Endpoint
```
GET http://localhost:8000/webhook/import-sales
```

---

## ✅ Pipeline Flow Summary

1. 🕓 Cron trigger in n8n
2. 🌐 Webhook call to FastAPI
3. 🧾 Python import script runs
4. 🧼 Data cleaned and inserted into DB
5. 📈 Dashboard updates
6. 📬 Slack/email notification if needed

---

## 📓 Log Example

```
2025-05-21 16:04:03 - INFO - Starting import process.
2025-05-21 16:04:04 - INFO - Imported 12 rows successfully.
```

Errors trigger an email alert.

---

## 💡 Next Steps

- Extend tests and error handling
- Add Docker Compose setup
- Deploy Streamlit dashboard publicly
