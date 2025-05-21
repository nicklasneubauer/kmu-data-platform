## 🚀 Release: v1.0.0 – Initial Public Version

This is the first full release of the **kmu-data-platform**, a modular, end-to-end data platform tailored for small businesses and consultants.

---

### ✨ Highlights

- ✅ CSV & API ingestion (manual + automated)
- 🧹 Data transformation with Pandas
- 🗃️ SQLite database via SQLAlchemy (PostgreSQL-ready)
- 📊 Streamlit Dashboard with customer filtering
- 📄 PDF export with embedded charts
- 🛠️ Admin dashboard: logs, DB status, manual import
- 🔁 n8n integration with webhook trigger
- 📬 Email alerts on import failure
- 🧾 Central log file: `import.log`

---

### 📦 Modules

| Module      | Description                            |
|-------------|----------------------------------------|
| ingestion   | Load CSV or fetch API data             |
| transform   | Clean & normalize datasets             |
| db          | Schema, import logic, logging & alert |
| dashboard   | Streamlit dashboards (user + admin)    |
| automation  | n8n workflows (cron, webhook, alert)   |
| webhook     | FastAPI trigger for import             |

---

### 🛠️ How to Run

1. Clone repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

Run Streamlit UI:

streamlit run dashboard/app.py
Start webhook (optional):

uvicorn webhook_server:app --reload

📝 Environment Variables (.env)

ALERT_EMAIL_FROM=alerts@yourdomain.com
ALERT_EMAIL_TO=admin@yourdomain.com
SMTP_SERVER=smtp.yourdomain.com
SMTP_PORT=587

📈 Demo Use Case
Automated monthly import of sales reports with PDF summaries for each client, visualized in Streamlit and controlled via admin interface.

📣 Feedback
Found a bug or have a feature idea?
Open an issue or contribute via pull request!

🔖 Tag: v1.0.0
📅 Date: {{ release_date }}

yaml
Copy
Edit
