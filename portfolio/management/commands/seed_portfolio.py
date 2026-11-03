from django.core.management.base import BaseCommand
from portfolio.models import Profile, SkillCategory, Skill, Education, ProjectCategory, Project

class Command(BaseCommand):
    help = "Seed database with initial portfolio data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding portfolio data...")

        # 1. Profile
        Profile.objects.all().delete()
        profile = Profile.objects.create(
            full_name="Jainam Sheth",
            title="Full Stack Developer & Software Engineer",
            subtitle_roles="Full Stack Developer, Django Specialist, Python Engineer",
            bio="I architect robust backends, design intuitive frontends, and create seamless web experiences using Django, modern JavaScript, and clean coding standards.",
            about_text=(
                "I am a dedicated software developer specializing in Python, Django, modern JavaScript, and responsive web design. "
                "I enjoy turning complex system designs into clean, maintainable, and user-centric web applications. "
                "Whether crafting RESTful APIs, optimizing relational databases, or styling pixel-perfect user interfaces, "
                "I bring technical precision and artistic care to every project."
            ),
            avatar_url="/static/images/profile.png",
            email="jainamsheth2006@gmail.com",
            phone="+91 9924377710",
            location="Ahmedabad",
            github_url="https://github.com/Jainamsheth06",
            linkedin_url="https://www.linkedin.com/in/jainam--sheth",
            twitter_url="https://x.com/jainam216sheth",
            completed_projects=5,
            happy_clients=5,
            satisfaction_rate=100,
            available_for_hire=True,
        )
        self.stdout.write(f"Created Profile: {profile.full_name}")

        # 2. Skill Categories & Skills
        SkillCategory.objects.all().delete()

        skills_data = [
            {
                "category": "Backend Engineering",
                "icon": "fa-solid fa-server",
                "order": 1,
                "skills": [
                    ("Python", 95, "fa-brands fa-python"),
                    ("Django / Django REST Framework", 92, "fa-solid fa-code"),
                    ("RESTful API Architecture", 90, "fa-solid fa-network-wired"),
                    ("SQL & SQLite", 88, "fa-solid fa-database"),
                ]
            },
            {
                "category": "Frontend & UI/UX",
                "icon": "fa-solid fa-laptop-code",
                "order": 2,
                "skills": [
                    ("HTML5 & Semantic Markup", 95, "fa-brands fa-html5"),
                    ("Modern CSS3 & Flex/Grid", 92, "fa-brands fa-css3-alt"),
                    ("JavaScript (ES6+) & DOM", 88, "fa-brands fa-js"),
                    ("Responsive Web Design", 94, "fa-solid fa-mobile-screen"),
                    ("Tailwind / Modern Frameworks", 85, "fa-solid fa-palette"),
                ]
            },
            {
                "category": "Tools & Version Control",
                "icon": "fa-solid fa-code-branch",
                "order": 3,
                "skills": [
                    ("Git & Version Control", 92, "fa-brands fa-git-alt"),
                    ("CI/CD Pipelines (GitHub Actions)", 78, "fa-solid fa-gears"),
                ]
            },
            {
                "category": "Soft Skills",
                "icon": "fa-solid fa-lightbulb",
                "order": 4,
                "skills": [
                    ("Logical Thinking", 92, "fa-solid fa-brain"),
                    ("Problem Solving", 95, "fa-solid fa-puzzle-piece"),
                    ("Team Work", 90, "fa-solid fa-people-group"),
                    ("Oral & Written Communication", 88, "fa-solid fa-comments"),
                ]
            }
        ]

        for cat_data in skills_data:
            cat = SkillCategory.objects.create(
                name=cat_data["category"],
                icon=cat_data["icon"],
                order=cat_data["order"]
            )
            for skill_order, (name, pct, icon) in enumerate(cat_data["skills"], start=1):
                Skill.objects.create(
                    category=cat,
                    name=name,
                    percentage=pct,
                    icon_class=icon,
                    order=skill_order
                )
        self.stdout.write("Created Skill Categories and Skills.")

        # 3. Education & Certifications
        Education.objects.all().delete()
        educations = [
            {
                "degree": "Full Stack Python & Django Web Development",
                "institution": "Tops Technologies",
                "location": "Ahmedabad, Gujarat",
                "start_year": "2025",
                "end_year": "Present",
                "description": "Intensive hands-on practical track covering Django MVC architecture, RESTful API development, SQL, SQLite database management, JavaScript DOM manipulation, and responsive web design.",
                "order": 1
            },
            {
                "degree": "Bachelor of Science - Computer Science & Information Technology",
                "institution": "Silver Oak University",
                "location": "Ahmedabad, Gujarat",
                "start_year": "2024",
                "end_year": "Present",
                "gpa": "8.18",
                "description": "Gaining the basic knowledge of coding.",
                "order": 2
            },
            {
                "degree": "Higher Secondary Certificate (HSC - 12th)",
                "institution": "Shayona VidhyaVihar Higher Secondary School (GSEB)",
                "location": "Ahmedabad, Gujarat",
                "start_year": "2022",
                "end_year": "2024",
                "gpa": "44%",
                "description": "Completed Higher Secondary with focus on Physics, Chemistry, Mathematics",
                "order": 3
            },
            {
                "degree": "Secondary School Certificate (SSC - 10th)",
                "institution": "Excelsior Model High School (GSEB)",
                "location": "Adipur, Kutch, Gujarat",
                "start_year": "2020",
                "end_year": "2021",
                "gpa": "58%",
                "description": "Completed Secondary School",
                "order": 4
            }
        ]
        
        for edu in educations:
            Education.objects.create(**edu)
        self.stdout.write("Created Education records.")

        # 5. Project Categories & Projects
        ProjectCategory.objects.all().delete()
        Project.objects.all().delete()

        cat_fullstack = ProjectCategory.objects.create(name="Full Stack", slug="full-stack", order=1)
        cat_api = ProjectCategory.objects.create(name="RESTful APIs", slug="restful-apis", order=2)
        cat_webapps = ProjectCategory.objects.create(name="Web Apps", slug="web-apps", order=3)
        cat_cli = ProjectCategory.objects.create(name="Python & CLI", slug="python-cli", order=4)
        cat_security = ProjectCategory.objects.create(name="Security & Tools", slug="security-tools", order=5)

        projects_data = [
            {
                "category": cat_webapps,
                "title": "To-Do-List",
                "slug": "to-do-list",
                "short_description": "Interactive task management web application built with Python, Django, and JavaScript featuring real-time task creation and status filtering.",
                "detailed_description": (
                    "The To-Do-List application is an intuitive task management tool designed to streamline daily workflows. "
                    "Features dynamic task creation, instant completion toggles, categorical filters (All, Active, Completed), "
                    "and persistent database storage powered by Django ORM and clean responsive frontend design."
                ),
                "key_features": (
                    "Add, complete, edit, and delete tasks seamlessly\n"
                    "Filter tasks by All, Active, and Completed views\n"
                    "Responsive, mobile-friendly design with modern dark/light styling\n"
                    "Clean Django MVT architecture with robust form validation"
                ),
                "image_url": "/static/images/projects/todo-list.png",
                "technologies": "Django, Python, HTML5, CSS3, JavaScript, SQLite",
                "github_url": "https://github.com/Jainamsheth06/to-do-list",
                "live_demo_url": "",
                "featured": True,
                "order": 1
            },
            {
                "category": cat_fullstack,
                "title": "Hospital Management System",
                "slug": "hospital-management-system",
                "short_description": "Comprehensive healthcare administration system managing patient records, doctor appointments, billing, and departmental workflows.",
                "detailed_description": (
                    "The Hospital Management System is a full-featured clinical management solution developed with Django and Python. "
                    "It streamlines hospital operations by coordinating outpatient and inpatient admissions, appointment scheduling with doctors, "
                    "medical department categorization, and automated invoice billing."
                ),
                "key_features": (
                    "Patient registration, medical history, and status tracking\n"
                    "Doctor appointment scheduling with departmental categorization\n"
                    "Automated billing, invoicing, and patient management\n"
                    "Role-based access control for administrative staff and medical professionals"
                ),
                "image_url": "/static/images/projects/hospital-management.png",
                "technologies": "Django, Python, PostgreSQL, HTML5, CSS3, JavaScript, Bootstrap",
                "github_url": "https://github.com/Jainamsheth06/Hospital-Management-System",
                "live_demo_url": "",
                "featured": True,
                "order": 2
            },
            {
                "category": cat_cli,
                "title": "Auto-Sphere Car Rental System (Console App)",
                "slug": "auto-sphere-car-rental-system",
                "short_description": "Interactive terminal-based car rental and fleet management software developed in pure Python using Object-Oriented Programming (OOP) and menu-driven CLI workflows.",
                "detailed_description": (
                    "Auto-Sphere Car Rental System is a console-based vehicle rental management application developed with Python. "
                    "Built around core Object-Oriented Programming (OOP) principles, the system allows users to view live vehicle stock, rent cars across various categories (SUV, Sedan, EV), "
                    "calculate duration-based rental tariffs (hourly/daily), record customer bookings, and generate structured billing receipts directly through an interactive command-line interface."
                ),
                "key_features": (
                    "Interactive menu-driven terminal interface with user input validation\n"
                    "Object-Oriented Design (Car, Customer, RentalAgency, and Invoice classes)\n"
                    "Dynamic rental pricing calculation based on rental duration and vehicle tier\n"
                    "Vehicle stock returns, availability tracking, and automated receipt export"
                ),
                "image_url": "/static/images/projects/auto-sphere.png",
                "technologies": "Python, OOP (Object-Oriented Programming), CLI / Console, File Handling, Data Structures",
                "github_url": "https://github.com/Jainamsheth06/Auto-Sphere-Car-Rental-System",
                "live_demo_url": "",
                "featured": True,
                "order": 3
            },
            {
                "category": cat_security,
                "title": "IntegritySentinel",
                "slug": "integrity-sentinel",
                "short_description": "Advanced cybersecurity file and system integrity monitoring (FIM) tool tracking cryptographic hash baseline alterations and unauthorized file modifications.",
                "detailed_description": (
                    "IntegritySentinel is an automated cybersecurity and system integrity monitoring solution built with Python. "
                    "It continuously tracks critical directories and system files, computes cryptographic hashes (SHA-256), detects unauthorized modifications, injections, or file tampering, and triggers real-time alerts upon detecting security violations."
                ),
                "key_features": (
                    "Real-time file change, deletion, and injection monitoring\n"
                    "Cryptographic checksum verification (SHA-256 baseline)\n"
                    "Automated security alert logs and anomaly reports\n"
                    "Clean command-line and web dashboard interface"
                ),
                "image_url": "/static/images/projects/integrity-sentinel.png",
                "technologies": "Python, Cryptography, Hashing, Django, SQLite, Linux/Windows Security",
                "github_url": "https://github.com/Jainamsheth06/IntegritySentinel",
                "live_demo_url": "",
                "featured": True,
                "order": 4
            },
            {
                "category": cat_api,
                "title": "DoctorFinder (RESTful API)",
                "slug": "doctor-finder",
                "short_description": "Scalable Django REST Framework (DRF) backend API powering doctor discovery, specialty filtering, real-time consultation slots, and patient booking.",
                "detailed_description": (
                    "DoctorFinder RESTful API is an advanced backend web service engineered with Python and Django REST Framework (DRF). "
                    "It delivers clean, secure, and performant RESTful endpoints to query verified doctors by medical specialty and location, "
                    "check live appointment availability, handle booking transactions, and manage healthcare records with JSON serialization, "
                    "token-based authentication, and robust validation rules."
                ),
                "key_features": (
                    "RESTful CRUD API endpoints for doctors, specialties, and appointments\n"
                    "Django REST Framework serializers with input validation and error handling\n"
                    "Specialty, location, and rating filtering with query parameters\n"
                    "Token/Session authentication and optimized database queries with pagination\n"
                    "Interactive API documentation & Postman collection support"
                ),
                "image_url": "/static/images/projects/doctor-finder.png",
                "technologies": "Django REST Framework, Python, RESTful APIs, SQL, SQLite, JSON, Postman",
                "github_url": "https://github.com/Jainamsheth06/module-9--Python---DB-and-Python-Framework",
                "live_demo_url": "",
                "featured": True,
                "order": 5
            }
        ]

        for p_data in projects_data:
            cat = p_data.pop("category")
            if isinstance(cat, str):
                cat = ProjectCategory.objects.get(name=cat)
            Project.objects.create(category=cat, **p_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded rich portfolio database!"))

