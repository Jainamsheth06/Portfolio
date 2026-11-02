# 🚀 Developer Portfolio & Resume (Django + HTML5 + CSS3 + JS)

A modern, responsive, full-stack Developer Portfolio & Resume website built with **Django**, **HTML5**, **CSS3**, and **JavaScript**.

---

## ✨ Features

- 🌓 **Dark & Light Mode Switcher**: Smooth transitions with `localStorage` persistence.
- ⌨️ **Dynamic Typewriter Hero**: Rotating headline badges showcasing your roles.
- ⚡ **Interactive Stats Counter**: Animated number increments on scroll.
- 🎯 **Filterable Project Showcase**: Instant category filtering ("All", "Full Stack", "Web Apps", "APIs") with modal previews.
- 🔍 **Interactive Project Modal**: Displays full project overview, key highlights, tech stack tags, live demo, and GitHub links.
- 📊 **Animated Skill Progress Bars**: Responsive skill meters with percentage indicators.
- 💼 **Dual Career Timeline**: Tabbed switcher between "Work Experience" and "Education & Certifications".
- 📩 **AJAX Contact Form**: Non-reloading message submission with real-time feedback and validation.
- 🛠️ **Full Django Admin Control**: Easily update profile information, add projects, modify skills, and view contact submissions via the web admin interface.
- 📱 **100% Mobile & Tablet Responsive**: Optimized from small screens to ultra-wide displays.

---

## 📁 Project Structure

```text
Portfolio-Resume/
├── .venv/                      # Python virtual environment
├── core/                       # Django project root configuration
│   ├── settings.py             # App settings, static & media definitions
│   ├── urls.py                 # Core routing
│   └── wsgi.py
├── portfolio/                  # Main Portfolio application
│   ├── management/commands/
│   │   └── seed_portfolio.py   # Seeder script with rich initial data
│   ├── migrations/             # Database migrations
│   ├── admin.py                # Django Admin customizations
│   ├── forms.py                # Contact form definition
│   ├── models.py               # Profile, Skills, Projects, Experience, Contact models
│   ├── tests.py                # Automated unit tests
│   ├── urls.py                 # Portfolio routes and API endpoints
│   └── views.py                # Controller views & JSON API
├── static/
│   ├── css/
│   │   └── style.css           # Glassmorphic, modern CSS with themes
│   └── js/
│       └── main.js             # Theme toggle, typewriter, modals, AJAX
├── templates/
│   └── portfolio/
│       ├── base.html           # Master layout (Navbar, Footer, Modals)
│       └── index.html          # Main single-page portfolio layout
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django CLI tool
└── requirements.txt            # Python dependencies
```

---

## 🚀 Quick Start Guide

### 1. Activate the Virtual Environment

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.\.venv\Scripts\activate.bat
```

---

### 2. Run Database Migrations (Already configured)

```powershell
python manage.py migrate
```

---

### 3. (Optional) Re-seed Portfolio Data

To reset or populate fresh sample portfolio data at any time:

```powershell
python manage.py seed_portfolio
```

---

### 4. Start the Development Server

```powershell
python manage.py runserver
```

Open your browser and navigate to:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

### 5. Access the Django Admin Panel

You can manage all your portfolio content (Personal details, projects, skills, messages) through the built-in admin dashboard:

- **URL:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Username:** `admin`
- **Password:** `admin123`

*(You can change the password at any time via `python manage.py changepassword admin`)*

---

## 🧪 Running Tests

To run the automated test suite:

```powershell
python manage.py test
```

