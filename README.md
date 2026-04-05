# Expense Tracker

A full-stack personal finance application built with **Django** and **Bootstrap**. Track your daily expenses, organize them by category, and get an instant overview of your total spending — all from a clean, responsive web dashboard.

---

## Features

- **Add Expenses** — Log an expense with amount, category, date, and description
- **View All Expenses** — See all recorded expenses in a sortable, striped table
- **Total Spending Summary** — Instantly view total expenditure at the top of the dashboard
- **Category-wise Breakdown** — Expenses are grouped and summarized by category
- **Delete Expenses** — Remove any expense entry with a single click
- **Responsive UI** — Built with Bootstrap 5 for a clean look on any device

---

## Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Backend   | Python 3, Django        |
| Frontend  | Django Templates, Bootstrap 5 |
| Database  | SQLite3                 |

---

## Project Structure

```
expense_tracker/
├── expense_tracker/          # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── trackerapp/               # Main application
│   ├── models.py             # Expense model
│   ├── views.py              # Home, Add, Delete views
│   ├── urls.py               # App URL routes
│   ├── admin.py              # Admin registration
│   ├── migrations/           # Database migrations
│   └── templates/
│       ├── base.html         # Base layout
│       └── trackerapp/
│           ├── home.html     # Dashboard
│           └── add_expense.html
├── db.sqlite3                # SQLite database
└── manage.py
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker/expense_tracker
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install django
```

**4. Apply database migrations**

```bash
python manage.py migrate
```

**5. Run the development server**

```bash
python manage.py runserver
```

**6. Open in your browser**

```
http://127.0.0.1:8000
```

---

## Data Model

### `Expense`

| Field         | Type          | Description                    |
|---------------|---------------|--------------------------------|
| `id`          | AutoField     | Primary key (auto-generated)   |
| `amount`      | FloatField    | Expense amount                 |
| `category`    | CharField     | Category label (e.g. Food)     |
| `date`        | DateField     | Date of the expense            |
| `description` | TextField     | Optional note (can be blank)   |

---

## URL Routes

| URL                    | View             | Description             |
|------------------------|------------------|-------------------------|
| `/`                    | `home`           | Dashboard               |
| `/add/`                | `add_expense`    | Add a new expense       |
| `/delete/<id>/`        | `delete_expense` | Delete an expense by ID |

---

## Screenshots

> _Add screenshots of the dashboard and add-expense page here._

---

## Future Enhancements

- User authentication and multi-user support
- Monthly budget setting with overspend alerts
- Expense filtering by category, date, and amount range
- Monthly summary export to CSV
- Charts and analytics using Chart.js or Matplotlib

---

## License

This project is open-source and available under the [MIT License](LICENSE).

## Author

Soham Dongare  
Aspiring Full Stack Developer (Python)
<p>
  Connect with me:
  <a href="https://www.linkedin.com/in/soham-dongare/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?logo=linkedin" />
  </a>
</p>