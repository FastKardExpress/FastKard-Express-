from twilio.rest import Client

# Twilio credentials
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms(to_number, message):
    from_number = "YOUR_TWILIO_NUMBER"
    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    print(f"Message sent successfully! SID: {message.sid}")

if __name__ == "__main__":
    to = input("Enter receiver phone number with country code (+91...): ")
    msg = input("Enter your message: ")
    send_sms(to, msg)
