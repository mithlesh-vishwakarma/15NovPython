# Django Assignment: Practical Implementation Guide (Session 2)

This guide provides step-by-step instructions, commands, exact file structures, and complete copy-pasteable code files to implement the Django `playlists` app.

---

## 1. Project Directory File Structure

After completing all the setup steps, your directory structure under `session-2/practical` will look like this:

```text
session-2/practical/
│
├── manage.py                     # Project-level CLI manager
├── db.sqlite3                    # Database file (automatically created)
│
├── myenv/                        # Virtual Environment directory
│   └── ...
│
├── foodiehub_project/            # Main Django Configuration Project Directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # MODIFIED: Registered playlists app
│   ├── urls.py                   # MODIFIED: Mapped music/ route
│   └── wsgi.py
│
└── playlists/                    # NEW: Django App Directory
    ├── migrations/               # Database migrations folder
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py                  # Standard admin configuration
    ├── apps.py                   # Standard app metadata definition
    ├── models.py                 # Database models
    ├── tests.py                  # Unit testing functions
    └── views.py                  # NEW: Defined home view returning response
```

---

## 2. Step-by-Step Terminal Commands

Follow these steps sequentially to setup and launch your app.

### Step A: Open Terminal and Navigate to Project Directory
Ensure your terminal is pointed at the workspace directory:
```bash
cd "d:\projects\Tops-Projects(assignments)\15NovPython\Python\Assignments\Module-9\session-2\practical"
```

### Step B: Activate the Virtual Environment
Activate the pre-configured virtual environment `myenv` on Windows:
```powershell
.\myenv\Scripts\activate
```

### Step C: Create the `playlists` App
Run the standard Django app creation command:
```bash
python manage.py startapp playlists
```
*This command creates the `playlists` folder structure automatically.*

---

## 3. Exact Code files to Copy-Paste

All the code blocks below contain beginner-friendly comments and can be copied directly into your VS Code workspace.

### File 1: View Definition
**File Path:** `playlists/views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse  # Import HttpResponse to return plain text/HTML responses

# Create your views here.

def home(request):
    """
    A simple Django view function.
    
    Arguments:
        request: The HTTP Request object containing metadata about the browser's request.
        
    Returns:
        HttpResponse: A response containing the welcome text.
    """
    # Return the Spotify Playlists greeting message with Mithlesh's name
    return HttpResponse("Welcome to My Spotify Playlists! - Mithlesh")
```

---

### File 2: App Registration
**File Path:** `foodiehub_project/settings.py`
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom apps
    'playlists',  # Registering the new 'playlists' app
]
```

---

### File 3: URL Routing
**File Path:** `foodiehub_project/urls.py`
```python
"""
URL configuration for foodiehub_project project.
"""
from django.contrib import admin
from django.urls import path
from playlists import views as playlist_views  # Import the views module from playlists app

urlpatterns = [
    # Mapped Django Admin Panel
    path('admin/', admin.site.urls),
    
    # Map the URL path 'music/' to the home view function from the playlists app
    path('music/', playlist_views.home, name='music-home'),
]
```

---

## 4. How to Run the Server

To start the local Django development server, run the following command in your activated terminal:
```bash
python manage.py runserver
```

**Expected Startup Output:**
```text
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 15, 2026 - 13:58:12
Django version 6.0.6, using settings 'foodiehub_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK (or CTRL-C).
```

---

## 5. How to Restart the Server

*   **Automatic Restart (Real-Time Auto-Reloading)**: You do **not** need to manually restart the server when modifying python or html files. Django’s built-in file-watcher will detect file modifications upon saving (`CTRL + S`) and reload the environment automatically.
*   **Manual Restart**: If you run into database migration changes or server blocks, press `CTRL + C` inside the running terminal to terminate the server, and then run `python manage.py runserver` again.

---

## 6. Expected Final Output & Browser URL

### Browser URL
To view the output, open your web browser and navigate to:
```text
http://localhost:8000/music/
```
*(Alternative URL: `http://127.0.0.1:8000/music/`)*

### Visual/Text Representation of Browser Output
```text
┌──────────────────────────────────────────────────────────┐
│  🌐 http://localhost:8000/music/                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Welcome to My Spotify Playlists! - Mithlesh             │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 7. Assignment Submission Conclusion

By completing this assignment:
1. We successfully instantiated a modular Django App named `playlists` within our existing `foodiehub_project` structure.
2. The auto-generated structure of `playlists` was registered in `settings.py`'s `INSTALLED_APPS` to activate it.
3. We implemented an HTTP request handling view inside `views.py` returning `"Welcome to My Spotify Playlists! - Mithlesh"`.
4. We successfully configured the routing middleware in `urls.py` by mapping requests pointing to `music/` directly to the view handler, ensuring a dynamic web application response flow.
