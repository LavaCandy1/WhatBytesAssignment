# Healthcare Backend API

Backend system for a healthcare application built for an assignment at Whatbytes.  
Provides secure **JWT authentication** and **role-based access control (RBAC)** for managing doctors, patients, and their mappings.

## Core Features

- **Authentication:** JWT-based login and registration.
- **Role-Based Access:** `Admin` and `Staff` roles with distinct permissions.
- **API Resources:** Full CRUD endpoints for Doctors, Patients, and their mapping.
- **Tech Stack:** Django, DRF, PostgreSQL.

---

## Quick Start

### 1. Prerequisites

- Python 3.8+
- PostgreSQL

### 2. Setup

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd HealthcareBackend
    ```

2.  **Install dependencies:**

    ```bash
    python -m venv venv
    # Activate venv (use venv\Scripts\activate on Windows)
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Configure environment:**

    - Create a `.env` file in the root directory.
    - Copy the contents from the example below and add your database credentials.

    ```ini
    # .env example
    SECRET_KEY='your-secret-key'
    DB_NAME=Healthcare
    DB_USER=postgres
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    ```

4.  **Run the application:**

    ```bash
    # Set up the database
    python manage.py migrate

    # Create an admin user for testing admin-only APIs
    python manage.py createsuperuser

    # Start the server
    python manage.py runserver
    ```

    **Important:** Use the superuser to login and then use the access JWT token in header to access admin endpoints (all data modification endpoints).

The API will be running at `http://127.0.0.1:8000`.

---

## API Overview

The API provides endpoints for managing users, doctors, patients, and their relationships.

- `/api/auth/`: User registration and login.
- `/api/doctors/`: Doctor management (Admins only for creation/deletion).
- `/api/patients/`: Patient management (Staff & Admins).
- `/api/mappings/`: Assigning doctors to patients (Staff & Admins).

Important Notes -

- Remember to use the JWT token in the `Authorization: Bearer <token>` header to access protected routes.
- Admin users can create and delete doctors, while staff users can only view them.
- To get a user with Admin role you can create a superuser using the command `python manage.py createsuperuser` and then use that user to login and get the JWT token.
