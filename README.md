
```markdown
# Retain Coding Challenge Solutions

This repository contains solutions for two independent tasks:
1. **User Management API Refactor** (Task 1)
2. **URL Shortener Service** (Task 2)

---

## Task 1: User Management API Refactor

### Overview
Refactored a legacy user management API to improve security, structure, and maintainability while preserving all existing functionality.

### Key Improvements
- ✅ Implemented password hashing (bcrypt)
- ✅ Added JWT authentication
- ✅ Restructured project with proper separation of concerns
- ✅ Enhanced error handling and status codes
- ✅ Added basic test coverage

### API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/users` | POST | Create new user |
| `/users` | GET | List all users |
| `/user/<id>` | GET | Get specific user |
| `/user/<id>` | PUT | Update user |
| `/user/<id>` | DELETE | Delete user |
| `/login` | POST | User authentication |

### Setup
```bash
cd user-management-refactor
pip install -r requirements.txt
python app.py
```

### Testing
```bash
pytest tests/
```

---

## Task 2: URL Shortener Service

### Overview
A Flask-based URL shortening service with analytics tracking.

### Features
- Generate 6-character short codes
- Redirect with click tracking
- View analytics (clicks, creation time)
- Input validation

### API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/shorten` | POST | Create short URL |
| `/<short_code>` | GET | Redirect to original URL |
| `/api/stats/<short_code>` | GET | Get analytics |

### Setup
```bash
cd url-shortener
pip install -r requirements.txt
python -m flask --app app.main run
```

### Example Usage
```bash
# Shorten URL
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'

# Redirect
curl -L http://localhost:5000/abc123

# Get stats
curl http://localhost:5000/api/stats/abc123
```

### Testing
```bash
pytest -v
```

---

## Repository Structure
```
retain-challenge/
├── user-management-refactor/  # Task 1 Solution
│   ├── app/                   # Refactored application
│   ├── tests/                 # Test cases
│   ├── CHANGES.md             # Refactoring documentation
│   └── requirements.txt
│
└── url-shortener/             # Task 2 Solution
    ├── app/                   # Flask application
    ├── tests/                 # Test cases
    └── requirements.txt
```

## Requirements
- Python 3.8+
- pip

## Notes
- Both solutions use in-memory storage for demonstration purposes
- Includes all required tests and documentation
- Production deployments would require:
  - Persistent database (PostgreSQL/Redis)
  - Proper secret management
  - WSGI server (Gunicorn/Uvicorn)

```

### Key Features of This README:
1. **Clear Separation** of both tasks
2. **Consistent Structure** for each project:
   - Overview
   - Key Features/Improvements
   - API Documentation
   - Setup Instructions
3. **Production Notes** highlighting what would be needed for real-world deployment
4. **Repository Structure** visualization
5. **Testing Instructions** for both projects

You can:
1. Copy this exactly as is
2. Add your GitHub repo link where indicated
3. Include any additional notes about your specific implementation in the `CHANGES.md` for Task 1

Would you like me to add any specific details about:
- Deployment instructions (Docker, etc.)?
- Additional security considerations?
- Extended test coverage reports?
