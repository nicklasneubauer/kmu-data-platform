import streamlit as st
import os
import sqlite3
import pandas as pd
from datetime import datetime
import subprocess

st.set_page_config(page_title="Admin Panel", layout="wide")
st.title("🛠️ Admin Dashboard")

DB_PATH = "kmu_sales.db"

# Datenbankstatus
st.subheader("📦 Datenbankübersicht")

if os.path.exists(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    st.write(f"Last Update: {df['date'].max()}")
    st.write(f"Total Records: {len(df)}")
    st.write(f"Total Customers: {df['customer'].nunique()}")
else:
    st.warning("Database not found.")

# Import auslösen
st.subheader("🔁 Pipeline manuell starten")
if st.button("Datenimport auslösen"):
    try:
        result = subprocess.run(["python", "db/import_data.py"], capture_output=True, text=True, check=True)
        st.success("✅ Import erfolgreich gestartet.")
        st.code(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error("❌ Fehler beim Import.")
        st.code(e.stderr)

# Logs anzeigen
st.subheader("📋 Logs anzeigen (optional)")
LOG_FILE = "import.log"
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        logs = f.read()
    st.text_area("Import Logs", logs, height=200)
else:
    st.info("Noch keine Logdatei vorhanden.")
