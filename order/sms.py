import africastalking

africastalking.initialize(
    username='sandbox',
    api_key='28f1d8454e349f0cebf0dd75a08e9a37e3dfb4dc4b81878931449eda93acd57d'
)

sms = africastalking.SMS

def sending(recipients ):
    # Set your message
    message = "Order was added successfully!"
    # Set your shortCode or senderId
    sender = "Sa_vannah"
    try:
        response = sms.send(message, recipients, sender)
        print (response)
    except Exception as e:
        print (f'we have a problem: {e}')
