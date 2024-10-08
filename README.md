# Application Microservice

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![SendGrid](https://img.shields.io/badge/SendGrid-3370FF?style=for-the-badge&logo=sendgrid&logoColor=white)

This project consists of a Flask application for managing job applications and a Google Cloud Function for sending email notifications about application status updates.

## Project Structure

```
Application-FlaskApp/
├── application.py
├── app.yaml
├── requirements.txt
└── app_update_sendgrid_cloud_function/
    └── app_update_sendgrid.py
```

## Flask Application (application.py)

### Features

- CRUD operations for job applications
- Get all applications
- Get application by ID
- Get total count of applications
- Get applications by recruiter email
- Get applications by jobseeker email
- Create new application
- Update application status
- Withdraw (delete) application

### Tech Stack

- 🐍 Python
- 🌶️ Flask
- 🐘 PostgreSQL
- ☁️ Google Cloud Pub/Sub

### Setup

1. Install required packages:
   ```
   pip install -r requirements.txt
   ```

2. Set up Google Cloud project and Pub/Sub topic

3. Configure the database connection in the script

### API Endpoints

- `GET /`: Health check
- `GET /application/`: Get all applications
- `GET /application/<application_id>`: Get application by ID
- `GET /application/total_count`: Get total count of applications
- `GET /application/recruiters/<recruiterEmail>`: Get applications by recruiter email
- `GET /application/jobseekers/<jobseekerEmail>`: Get applications by jobseeker email
- `POST /application`: Create new application
- `PUT /application/<application_id>/status`: Update application status
- `DELETE /application/<application_id>`: Withdraw application

### Deployment

The application is designed to be deployed on Google App Engine. Use the `app.yaml` file for configuration.

## Cloud Function (app_update_sendgrid.py)

### Features

- Triggered by Pub/Sub messages
- Sends email notifications using SendGrid when application status is updated

### Tech Stack

- 🐍 Python
- ☁️ Google Cloud Functions
- 📧 SendGrid

### Setup

1. Set up a Google Cloud Function triggered by the Pub/Sub topic used in the Flask app
2. Configure SendGrid API key

### Functionality

The function:
1. Receives a message from Pub/Sub containing application update information
2. Parses the message data
3. Constructs an email using SendGrid
4. Sends the email notification

## Deployment

1. Deploy the Flask application to Google App Engine
2. Deploy the Cloud Function to Google Cloud Functions

## Security Note

🔒 Ensure proper security measures are implemented before deploying this application in a production environment, especially regarding database credentials and API keys.

## Additional Notes

- The SendGrid API key in the cloud function code should be properly secured using environment variables or secret management.
- The email sending functionality currently uses a hardcoded sender and recipient for testing purposes. This should be updated for production use.
