# Bus Ticket Booking System API 🚌

A robust, RESTful backend API for a Bus Ticket Booking System built with **Django** and **Django REST Framework (DRF)**. This system features token-based authentication, automated seat generation upon bus registration, and secure booking mechanisms.

---

## 🚀 Key Features

*   **User Management & Authentication**: Secure registration and login using Django REST Framework Token Authentication.
*   **Bus Management**: Full CRUD endpoints to manage buses (routes, timings, seat capacity, pricing, features).
*   **Automatic Seat Allocation**: Real-time seat creation via Django signals. When a new bus is registered, seats (e.g. `S1`, `S2`...) matching the bus's capacity are automatically created.
*   **Secure Seat Booking**: Prevents double bookings and ensures only authenticated users can book available seats.
*   **User Bookings History**: View booking history restricted to the authenticated user.
*   **CORS Configuration**: Configured to work seamlessly with modern frontend frameworks (e.g., React/Vite running on `http://localhost:5173`).

---

## 🛠️ Technology Stack

*   **Backend Framework**: Django 6.0+
*   **API Framework**: Django REST Framework (DRF)
*   **Database**: MySQL
*   **Authentication**: Token Authentication (`rest_framework.authtoken`)
*   **Cross-Origin Requests**: Django CORS Headers (`django-cors-headers`)

---

## 📂 Project Structure

```text
travels/
│
├── booking/                # Main Django Application
│   ├── migrations/         # Database migrations
│   ├── admin.py            # Django Admin site registrations
│   ├── apps.py             # App-specific configuration & signal registration
│   ├── models.py           # Database models (Bus, Seat, Booking, Payment)
│   ├── serializers.py      # DRF Serializers for validation & representation
│   ├── signals.py          # Django Signals (automatic seat creation)
│   ├── urls.py             # App-specific API routes
│   └── views.py            # API request handlers (DRF Views/APIViews)
│
├── travels/                # Project Configuration
│   ├── settings.py         # Global project configurations
│   ├── urls.py             # Core routing entrypoint
│   ├── asgi.py & wsgi.py   # Deployment gateways
│   └── __init__.py
│
├── manage.py               # Django CLI management script
├── requirements.txt        # Python dependency list
├── .gitignore              # Git ignore rules for Django
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

Follow these steps to run the backend application locally:

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd travels
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies cleanly:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
Apply the migrations to set up your SQLite database schema:
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
To access the Django Admin Dashboard (`http://127.0.0.1:8000/admin/`), create an admin account:
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
Start the server locally:
```bash
python manage.py runserver
```
