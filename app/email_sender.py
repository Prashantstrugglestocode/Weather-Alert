import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SMTP_SERVER = os.getenv('SMTP_SERVER').strip()  # e.g., 'smtp.mail.yahoo.com'
SMTP_PORT = os.getenv('SMTP_PORT', 587)    # Default TLS port is 587
EMAIL_USER = os.getenv('EMAIL_USER').strip()
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD').strip()

def send_email(recipient: str, subject: str, body: str):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = recipient

    try:
        logging.info(f"Connecting to SMTP server {SMTP_SERVER} on port {SMTP_PORT} (TLS).")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.set_debuglevel(1)  # Enable debug output
            server.starttls()  # Upgrade the connection to secure TLS
            logging.info("Starting TLS.")
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            logging.info(f"Logged in as {EMAIL_USER}.")
            server.sendmail(EMAIL_USER, recipient, msg.as_string())
            logging.info(f"Email sent to {recipient}.")
    
    except smtplib.SMTPException as e:
        logging.error(f"SMTPException occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise

