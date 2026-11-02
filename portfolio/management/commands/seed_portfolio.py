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
            avatar_url="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80",
            email="jainamsheth2006@gmail.com",
            phone="+91 9924377710",
            location="Ahmedabad",
            github_url="https://github.com/Jainamsheth06",
            linkedin_url="https://www.linkedin.com/in/jainam--sheth",
            twitter_url="https://x.com/jainam216sheth",
            completed_projects=10,
            happy_clients=5,
            satisfaction_rate=100,
            available_for_hire=True,
            is_active=True
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
                    ("PostgreSQL / SQLite", 88, "fa-solid fa-database"),
                    ("Celery & Redis Caching", 82, "fa-solid fa-bolt"),
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
                "category": "DevOps & Cloud",
                "icon": "fa-solid fa-cloud",
                "order": 3,
                "skills": [
                    ("Docker & Containerization", 80, "fa-brands fa-docker"),
                    ("Git & Version Control", 92, "fa-brands fa-git-alt"),
                    ("Linux & Bash Scripting", 84, "fa-brands fa-linux"),
                    ("CI/CD Pipelines (GitHub Actions)", 78, "fa-solid fa-gears"),
                    ("Nginx & Gunicorn Deployment", 82, "fa-solid fa-server"),
                ]
            },
            {
                "category": "Methodologies & Tools",
                "icon": "fa-solid fa-screwdriver-wrench",
                "order": 4,
                "skills": [
                    ("Agile / Scrum Collaboration", 90, "fa-solid fa-people-group"),
                    ("Unit Testing & Pytest", 86, "fa-solid fa-vial-circle-check"),
                    ("Web Security & CSRF/XSS Defense", 88, "fa-solid fa-shield-halved"),
                    ("Performance Optimization & SEO", 85, "fa-solid fa-chart-line"),
                    ("Postman & API Documentation", 90, "fa-solid fa-book"),
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
                "degree": "Bachelor of Computer Applications / Computer Science",
                "institution": "Gujarat University / Institute of Technology",
                "location": "Ahmedabad, Gujarat",
                "start_year": "2023",
                "end_year": "Present",
                "gpa": "First Class",
                "description": "Core Coursework: Python & Web Programming, Relational Database Management Systems (RDBMS), Data Structures, Algorithms, Software Engineering.",
                "order": 1
            },
            {
                "degree": "Full Stack Python & Django Web Development",
                "institution": "Online Specialized Training & Hands-on Projects",
                "location": "Online",
                "start_year": "2024",
                "end_year": "2024",
                "gpa": "Certified",
                "description": "Intensive hands-on practical track covering Django MVC architecture, RESTful API development, PostgreSQL, JavaScript DOM manipulation, and responsive web design.",
                "order": 2
            },
            {
                "degree": "Higher Secondary Certificate (HSC - 12th)",
                "institution": "Gujarat Board (GSEB)",
                "location": "Ahmedabad, Gujarat",
                "start_year": "2021",
                "end_year": "2023",
                "gpa": "Distinction",
                "description": "Completed Higher Secondary with focus on Science, Mathematics, and Computer Applications.",
                "order": 3
            }
        ]
        for edu in educations:
            Education.objects.create(**edu)
        self.stdout.write("Created Education records.")

        # 5. Project Categories & Projects
        ProjectCategory.objects.all().delete()
        Project.objects.all().delete()

        cat_fullstack = ProjectCategory.objects.create(name="Full Stack", slug="full-stack", order=1)
        cat_webapps = ProjectCategory.objects.create(name="Web Apps", slug="web-apps", order=2)
        cat_apis = ProjectCategory.objects.create(name="APIs & Microservices", slug="apis", order=3)

        projects_data = [
            {
                "category": cat_fullstack,
                "title": "DevForge - Developer Workspace",
                "slug": "devforge-developer-workspace",
                "short_description": "Collaborative code snippet sharing, real-time reviews, and developer workspace built on Django and JavaScript.",
                "detailed_description": (
                    "DevForge is a full-featured collaborative platform built for engineering teams. It allows developers to create, "
                    "organize, and peer-review code snippets with syntax highlighting, version diffing, and tag-based discovery. "
                    "The backend leverages Django's robust ORM and security layers, while the frontend delivers a snappy, reactive user experience."
                ),
                "key_features": (
                    "Instant syntax-highlighted code sharing\n"
                    "Granular user permissions and team workspaces\n"
                    "Interactive comment threads on specific code lines\n"
                    "Automated tag indexing and full-text search"
                ),
                "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80",
                "technologies": "Django, Python, PostgreSQL, JavaScript, CSS3, Prism.js",
                "github_url": "https://github.com",
                "live_demo_url": "https://demo.example.com",
                "featured": True,
                "order": 1
            },
            {
                "category": "Web Apps",
                "title": "ShopSphere - E-Commerce Engine",
                "slug": "shopsphere-ecommerce-engine",
                "short_description": "Modern e-commerce platform with dynamic shopping cart, Stripe payment gateway, and customer order dashboard.",
                "detailed_description": (
                    "A production-ready e-commerce solution engineered with Django. Features multi-currency product catalogs, "
                    "real-time stock management, coupon code verification, and secure Stripe checkout flows. "
                    "Includes an administrative management dashboard for tracking orders, revenue metrics, and inventory alerts."
                ),
                "key_features": (
                    "Real-time cart calculation and stock deduction\n"
                    "End-to-end Stripe payment processing\n"
                    "Customer order history with downloadable PDF invoices\n"
                    "Product review and rating system"
                ),
                "image_url": "https://images.unsplash.com/photo-1557821552-17105176677c?auto=format&fit=crop&w=800&q=80",
                "technologies": "Django, Python, SQLite/PostgreSQL, HTML5, CSS3, JavaScript, Stripe API",
                "github_url": "https://github.com",
                "live_demo_url": "https://demo.example.com",
                "featured": True,
                "order": 2
            },
            {
                "category": "APIs & Microservices",
                "title": "PulseMetrics - API & System Monitor",
                "slug": "pulsemetrics-api-system-monitor",
                "short_description": "High-throughput API telemetry monitoring service with customizable health check endpoints and alert hooks.",
                "detailed_description": (
                    "PulseMetrics collects and computes real-time performance telemetry for microservices. Built with Django REST Framework "
                    "and Redis, it processes thousands of incoming status payloads per minute, visualizing latency distributions, status codes, "
                    "and uptime uptime percentages with interactive SVG and Canvas charts."
                ),
                "key_features": (
                    "Sub-10ms response logging pipeline\n"
                    "Automated email and webhook alert notifications on endpoint downtime\n"
                    "Interactive metrics dashboard with historical trends\n"
                    "Secure API key authentication and rate limiting"
                ),
                "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
                "technologies": "Django REST Framework, Python, Redis, Chart.js, Docker",
                "github_url": "https://github.com",
                "live_demo_url": "https://demo.example.com",
                "featured": True,
                "order": 3
            },
            {
                "category": "Web Apps",
                "title": "TaskFlow Pro - Agile Kanban Board",
                "slug": "taskflow-pro-agile-kanban",
                "short_description": "Intuitive drag-and-drop project tracker with sprint planning, task assignments, and activity timelines.",
                "detailed_description": (
                    "TaskFlow Pro delivers a seamless visual task management workflow. Utilizing HTML5 Drag and Drop API integrated with "
                    "Django asynchronous backend endpoints, users can move task cards across swimlanes, assign story points, tag colleagues, "
                    "and track project milestones."
                ),
                "key_features": (
                    "HTML5 Drag & Drop board with instant backend synchronization\n"
                    "Sprint velocity and burn-down chart generation\n"
                    "Custom labels, checklists, and file attachments\n"
                    "Dark/Light theme support with smooth micro-animations"
                ),
                "image_url": "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?auto=format&fit=crop&w=800&q=80",
                "technologies": "Django, Vanilla JS, HTML5 Drag/Drop, CSS Grid & Flexbox",
                "github_url": "https://github.com",
                "live_demo_url": "https://demo.example.com",
                "featured": False,
                "order": 4
            },
            {
                "category": "Full Stack",
                "title": "CryptaWatch - Portfolio & Alert Hub",
                "slug": "cryptawatch-portfolio-alert-hub",
                "short_description": "Real-time cryptocurrency portfolio tracker integrating live price streams, profit/loss calculations, and price alerts.",
                "detailed_description": (
                    "CryptaWatch is a real-time tracking dashboard for crypto assets. The application fetches live market quotes "
                    "from third-party APIs, computes weighted portfolio profit/loss margins, and provides automated browser alerts "
                    "when custom user-defined price thresholds are crossed."
                ),
                "key_features": (
                    "Live multi-asset price feed tracking\n"
                    "Dynamic P&L and asset allocation charts\n"
                    "Configurable price alerts via Web Push and Email\n"
                    "Historical valuation analytics"
                ),
                "image_url": "https://images.unsplash.com/photo-1621416894569-0f39ed31d247?auto=format&fit=crop&w=800&q=80",
                "technologies": "Django, Python, JavaScript, CSS3, External Financial APIs",
                "github_url": "https://github.com",
                "live_demo_url": "https://demo.example.com",
                "featured": False,
                "order": 5
            },
            {
                "category": "APIs & Microservices",
                "title": "EcoRoute - Geo-Logistics Routing Engine",
                "slug": "ecoroute-geo-logistics-engine",
                "short_description": "High-performance geospatial routing API calculating carbon-optimized delivery paths for commercial fleets.",
                "detailed_description": (
                    "EcoRoute is a specialized REST API that evaluates delivery routes against carbon emission models, road topologies, "
                    "and live traffic conditions. Fleet operators consume the API to cut fuel expenditures and minimize environmental footprints."
                ),
                "key_features": (
                    "Carbon footprint calculation per route waypoint\n"
                    "Comprehensive OpenAPI / Swagger interactive documentation\n"
                    "High-concurrency caching with Redis\n"
                    "JWT authentication and usage metering"
                ),
                "image_url": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
                "technologies": "Django REST Framework, Python, PostGIS, Swagger, Docker",
                "github_url": "https://github.com",
                "live_demo_url": "https://demo.example.com",
                "featured": False,
                "order": 6
            }
        ]

        for p_data in projects_data:
            cat = p_data.pop("category")
            if isinstance(cat, str):
                cat = ProjectCategory.objects.get(name=cat)
            Project.objects.create(category=cat, **p_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded rich portfolio database!"))

