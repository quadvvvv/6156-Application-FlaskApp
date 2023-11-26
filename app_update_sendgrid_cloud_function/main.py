import base64
import functions_framework
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import json

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def app_update_sendgrid(cloud_event):
    # # Print out the data from Pub/Sub, to prove that it worked
    # print(base64.b64decode(cloud_event.data["message"]["data"]))
     
    # Parse the JSON data
    data = base64.b64decode(cloud_event.data["message"]["data"])
    message_data = json.loads(data)

    # Extract relevant fields
    application_id = message_data['application_id']
    applicant_email = message_data['applicant_email']
    new_status = message_data['new_status']
    
    print(message_data)

    # SendGrid related
    SEND_GRID_API_KEY = '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'

    # hard coded to focalpoint's email for now
    message = Mail(
        from_email='qvduo2021@gmail.com',
        to_emails= 'yn2443@columbia.edu',
        subject= f"🎉 Application {application_id} Status Update",
        html_content= f"""
            <html>
            <body>
                <p>Dear {applicant_email},</p>
                <p>Your application status has been updated to: {new_status}</p>
            </body>
            </html>
            """
        )
        
    try:
        sg = SendGridAPIClient(SEND_GRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)



