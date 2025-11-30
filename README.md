# Job Board Backend API

This project is a professional backend for a Job Board platform, built with Django, Django REST Framework, PostgreSQL, JWT authentication, and Swagger/OpenAPI documentation.

## Features

- Modular Django apps: jobs, users, applications, categories
- JWT authentication (SimpleJWT)
- Role-based access control (admin, user)
- CRUD APIs for jobs, categories, applications
- Advanced job search and filtering (by title, location, category, company)
- PostgreSQL database
- Interactive API docs (Swagger UI, ReDoc)

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd alx-project-nexus
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv .venv
   & .venv\Scripts\Activate.ps1  # On Windows
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Create a `.env` file with your PostgreSQL credentials:
     ```env
     POSTGRES_DB=jobboard_db
     POSTGRES_USER=jobboard_user
     POSTGRES_PASSWORD=jobboard_pass
     POSTGRES_HOST=localhost
     POSTGRES_PORT=5432
     ```
5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
6. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```
7. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## API Usage

### Authentication

- Obtain JWT token:
  ```http
  POST /api/token/
  {
   "username": "<your_username>",
   "password": "<your_password>"
  }
  ```
- Use the token in the `Authorization` header:
  ```
  Authorization: Bearer <access_token>
  ```

### Endpoints

- `/api/jobs/` — CRUD and search jobs
- `/api/categories/` — CRUD categories
- `/api/applications/` — CRUD applications
- `/api/users/` — User-related endpoints

### Advanced Job Search

- Filter: `/api/jobs/?location=Nairobi&category=1`
- Search: `/api/jobs/?search=engineer`
- Order: `/api/jobs/?ordering=created_at`

### API Documentation

- Swagger UI: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- ReDoc: [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)

## Project Structure

```
alx-project-nexus/
├── jobs/
├── users/
├── applications/
├── categories/
├── jobboard_backend/
├── .env.example
├── requirements.txt
├── README.md
```

## License

MIT
