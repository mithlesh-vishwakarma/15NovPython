# PythonAnywhere Deployment & Postman Testing Guide

This guide details step-by-step instructions to deploy your Django REST API to **PythonAnywhere** and test the `/api/send-email/` endpoint using **Postman**.

---

## Step 1: Upload Code to PythonAnywhere

1. Log in to your [PythonAnywhere Account](https://www.pythonanywhere.com/).
2. Open a **Bash Console** from your Dashboard.
3. Upload or Clone your repository into your home directory:
   ```bash
   git clone <your-repository-url> session6-api
   cd session6-api
   ```

---

## Step 2: Set Up Virtual Environment & Install Dependencies

1. Create a virtual environment with Python 3:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 session6-venv
   ```
2. Install project dependencies:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt django-cors-headers python-dotenv requests stripe twilio google-auth
   ```

---

## Step 3: Configure Database & Static Files

1. Run Django migrations:
   ```bash
   python manage.py migrate
   ```
2. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

---

## Step 4: Configure Web App on PythonAnywhere

1. Navigate to the **Web** tab on PythonAnywhere and click **Add a new web app**.
2. Select **Manual configuration** and choose **Python 3.10**.
3. Under the **Virtualenv** section, set the path to your virtual environment:
   `/home/YOUR_USERNAME/.virtualenvs/session6-venv`
4. Under the **Code** section, set:
   - **Source code**: `/home/YOUR_USERNAME/session6-api`
   - **Working directory**: `/home/YOUR_USERNAME/session6-api`
5. Edit the **WSGI configuration file** (click on the link under WSGI configuration file) and replace its contents with:

   ```python
   import os
   import sys

   # Path to your project directory
   path = '/home/YOUR_USERNAME/session6-api'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'services_proj.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
   *(Replace `YOUR_USERNAME` with your actual PythonAnywhere username)*.

6. Click the green **Reload YOUR_USERNAME.pythonanywhere.com** button.

---

## Step 5: Test `/api/send-email/` Live using Postman

1. Open **Postman**.
2. Create a new **POST** request.
3. Set the request URL to your live PythonAnywhere URL:
   `https://YOUR_USERNAME.pythonanywhere.com/api/send-email/`
4. Go to the **Headers** tab and set:
   - `Content-Type`: `application/json`
5. Go to the **Body** tab, select **raw** -> **JSON**, and paste:
   ```json
   {
     "email": "user@example.com"
   }
   ```
6. Click **Send**.
7. You should receive a `200 OK` JSON response:
   ```json
   {
     "status": "success",
     "message": "Welcome email processed for user@example.com.",
     "mailgun_id": "<...>",
     "details": "..."
   }
   ```
8. **Submission Constraint**: Capture a full screenshot of the Postman window showing the request URL, JSON body, and the `200 OK` response payload to include in your final submission.
