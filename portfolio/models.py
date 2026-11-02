from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=120, default="Alex Morgan")
    title = models.CharField(max_length=200, default="Full Stack Developer & Software Engineer")
    subtitle_roles = models.CharField(
        max_length=300,
        default="Full Stack Developer, Django Specialist, Python Engineer, UI/UX Artisan",
        help_text="Comma-separated roles for animated typewriter effect"
    )
    bio = models.TextField(
        default="I build high-performance web applications, scalable backends, and intuitive user experiences with Django, modern JavaScript, and clean software architecture."
    )
    about_text = models.TextField(
        default="Hello! I'm a passionate developer with a strong foundation in full-stack web development. I specialize in building elegant, fast, and secure digital products. From designing relational database schemas and architecting RESTful APIs in Django to crafting fluid, responsive interfaces with HTML, CSS, and modern JavaScript, I love turning complex problems into clean, accessible code."
    )
    avatar = models.ImageField(upload_to="profile/", blank=True, null=True)
    avatar_url = models.CharField(
        max_length=500,
        blank=True,
        default="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80",
        help_text="Fallback photo URL if no local image is uploaded"
    )
    resume_file = models.FileField(upload_to="resumes/", blank=True, null=True)
    email = models.EmailField(default="alex.morgan@example.com")
    phone = models.CharField(max_length=40, default="+1 (555) 234-5678")
    location = models.CharField(max_length=150, default="San Francisco, CA / Remote")
    github_url = models.URLField(default="https://github.com", blank=True)
    linkedin_url = models.URLField(default="https://linkedin.com", blank=True)
    twitter_url = models.URLField(default="https://x.com", blank=True)
    leetcode_url = models.URLField(blank=True, default="https://leetcode.com")
    
    # Quick Stats
    experience_years = models.PositiveIntegerField(default=4)
    completed_projects = models.PositiveIntegerField(default=30)
    happy_clients = models.PositiveIntegerField(default=22)
    satisfaction_rate = models.PositiveIntegerField(default=99)
    available_for_hire = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.full_name


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, default="fa-solid fa-code")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(default=85)
    icon_class = models.CharField(max_length=100, default="fa-brands fa-python")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Experience(models.Model):
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    company_url = models.URLField(blank=True)
    location = models.CharField(max_length=150, blank=True, default="Remote")
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, default="Present")
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text="Key responsibilities and achievements")
    technologies = models.CharField(max_length=300, help_text="Comma-separated technologies used")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=180)
    institution = models.CharField(max_length=180)
    location = models.CharField(max_length=150, blank=True)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)
    gpa = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Project Categories"

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=280)
    detailed_description = models.TextField()
    key_features = models.TextField(blank=True, help_text="One feature per line")
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    image_url = models.CharField(
        max_length=500,
        blank=True,
        default="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
        help_text="Fallback screenshot URL"
    )
    technologies = models.CharField(max_length=250, help_text="Comma-separated tech tags")
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    @property
    def feature_list(self):
        if not self.key_features:
            return []
        return [f.strip() for f in self.key_features.split('\n') if f.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
