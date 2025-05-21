import pandas as pd
from sqlalchemy.orm import sessionmaker
from db.models import Sale, init_db
from transform.sample_transform import clean_sales_data
import logging
import smtplib
from email.message import EmailMessage
from datetime import datetime

LOG_FILE = "import.log"

def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def send_error_email(error_message):
    EMAIL_FROM = os.getenv("ALERT_EMAIL_FROM", "alert@example.com")
    EMAIL_TO = os.getenv("ALERT_EMAIL_TO", "admin@example.com")
    SMTP_SERVER = os.getenv("SMTP_SERVER", "localhost")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 25))

    msg = EmailMessage()
    msg.set_content(f"Data import failed:\n\n{error_message}")
    msg["Subject"] = "🚨 Data Import Failed"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.send_message(msg)
            logging.info("Error email sent.")
    except Exception as e:
        logging.error(f"Failed to send error email: {str(e)}")

def import_csv_to_db(csv_path="ingestion/example_sales.csv"):
    setup_logging()
    logging.info("Starting import process.")

    try:
        df = pd.read_csv(csv_path)
        df_clean = clean_sales_data(df)

        engine = init_db()
        Session = sessionmaker(bind=engine)
        session = Session()

        for _, row in df_clean.iterrows():
            sale = Sale(date=row["date"], customer=row["customer"], amount=row["amount"])
            session.add(sale)

        session.commit()
        session.close()

        logging.info(f"Imported {len(df_clean)} rows successfully.")
        print(f"✅ Imported {len(df_clean)} rows into the database.")
    except Exception as e:
        logging.error(f"Import failed: {str(e)}")
        send_error_email(str(e))
        print("❌ Import failed. See import.log for details.")

if __name__ == "__main__":
    import_csv_to_db()
