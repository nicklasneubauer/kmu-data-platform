import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from fpdf import FPDF
import datetime
import matplotlib.pyplot as plt

st.set_page_config(page_title="KMU Sales Dashboard", layout="wide")
st.title("📊 KMU Sales Dashboard")

# Datenbankverbindung
engine = create_engine("sqlite:///kmu_sales.db")
df = pd.read_sql("SELECT * FROM sales", engine)

# Mandantenfilter
customers = df["customer"].dropna().unique()
selected_customer = st.selectbox("Select customer", sorted(customers))

# Gefilterte Daten
filtered_df = df[df["customer"] == selected_customer]

# KPIs
st.metric("Total Sales", f"{filtered_df['amount'].sum():.2f} EUR")
st.metric("Records", len(filtered_df))

# Charts
st.subheader("Sales Over Time")
df_sorted = filtered_df.sort_values("date")
df_grouped = df_sorted.groupby("date")["amount"].sum()
st.line_chart(df_grouped)

# PNG-Export für Matplotlib Chart
def save_charts(customer_df, customer_name):
    line_path = f"line_{customer_name}.png"
    bar_path = f"bar_{customer_name}.png"

    # Line Chart
    customer_df_sorted = customer_df.sort_values("date")
    customer_df_grouped = customer_df_sorted.groupby("date")["amount"].sum()
    plt.figure(figsize=(6, 3))
    customer_df_grouped.plot(kind="line", title="Sales Over Time")
    plt.tight_layout()
    plt.savefig(line_path)
    plt.close()

    # Bar Chart
    plt.figure(figsize=(6, 3))
    bar_data = customer_df.groupby("customer")["amount"].sum()
    bar_data.plot(kind="bar", title="Sales by Customer")
    plt.tight_layout()
    plt.savefig(bar_path)
    plt.close()

    return line_path, bar_path

# PDF-Erstellung inkl. Charts
def generate_pdf(customer, total, count, line_path, bar_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Sales Report for {customer}", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Total Sales: {total:.2f} EUR", ln=True)
    pdf.cell(0, 10, f"Number of Records: {count}", ln=True)

    pdf.ln(10)
    pdf.image(line_path, x=10, w=180)
    pdf.ln(10)
    pdf.image(bar_path, x=10, w=180)

    filename = f"report_{customer}_{datetime.date.today()}.pdf"
    pdf.output(filename)
    return filename

if st.button("Generate PDF Report with Charts"):
    line_chart_path, bar_chart_path = save_charts(filtered_df, selected_customer)
    filename = generate_pdf(
        selected_customer,
        filtered_df["amount"].sum(),
        len(filtered_df),
        line_chart_path,
        bar_chart_path
    )
    st.success(f"PDF report '{filename}' generated!")
