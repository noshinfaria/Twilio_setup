from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


# Twilio credentials from console
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Search and "buy" 3 US numbers
for i in range(3):
    number = client.available_phone_numbers('US').local.list(
        sms_enabled=True, voice_enabled=True, limit=1)[0]

    print(f"Found: {number.friendly_name}")

    # Simulate purchase (commented out for trial)
    # purchased_number = client.incoming_phone_numbers \
    #     .create(phone_number=number.phone_number)
    # print(f"Purchased: {purchased_number.phone_number}")
