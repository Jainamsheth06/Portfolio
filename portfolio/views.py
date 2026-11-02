from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Profile, SkillCategory, Skill, Experience, Education, ProjectCategory, Project, ContactMessage
from .forms import ContactForm

def get_default_profile():
    return {
        'full_name': 'Alex Morgan',
        'title': 'Full Stack Developer & Software Engineer',
        'subtitle_roles': 'Full Stack Developer, Django Specialist, Python Engineer, UI/UX Artisan',
        'bio': 'I architect robust backends, design intuitive frontends, and create seamless web experiences using Django, modern JavaScript, and clean coding standards.',
        'about_text': "I am a dedicated software developer specializing in Python, Django, modern JavaScript, and responsive web design. I enjoy turning complex system designs into clean, maintainable, and user-centric web applications. Whether crafting RESTful APIs, optimizing relational databases, or styling pixel-perfect user interfaces, I bring technical precision and artistic care to every project.",
        'avatar_url': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80',
        'email': 'alex.morgan.dev@example.com',
        'phone': '+1 (555) 234-5678',
        'location': 'San Francisco, CA / Remote',
        'github_url': 'https://github.com',
        'linkedin_url': 'https://linkedin.com',
        'twitter_url': 'https://x.com',
        'leetcode_url': 'https://leetcode.com',
        'experience_years': 4,
        'completed_projects': 28,
        'happy_clients': 20,
        'satisfaction_rate': 99,
        'available_for_hire': True,
    }

def index(request):
    profile = Profile.objects.filter(is_active=True).first()
    if not profile:
        profile = get_default_profile()

    categories = SkillCategory.objects.prefetch_related('skills').all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.select_related('category').all()
    contact_form = ContactForm()

    context = {
        'profile': profile,
        'skill_categories': categories,
        'experiences': experiences,
        'educations': educations,
        'project_categories': project_categories,
        'projects': projects,
        'contact_form': contact_form,
    }
    return render(request, 'portfolio/index.html', context)

def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Accept', '')

        if form.is_valid():
            contact = form.save()
            msg = f"Thank you, {contact.name}! Your message has been received. I will get back to you shortly."
            if is_ajax:
                return JsonResponse({'status': 'success', 'message': msg})
            messages.success(request, msg)
            return redirect('/#contact')
        else:
            errors = form.errors.as_json()
            if is_ajax:
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
            messages.error(request, "There was an error in your submission. Please check the fields and try again.")
            return redirect('/#contact')

    return redirect('portfolio:index')

def project_detail_api(request, slug):
    project = get_object_or_404(Project, slug=slug)
    data = {
        'title': project.title,
        'category': project.category.name if project.category else 'Featured',
        'short_description': project.short_description,
        'description': project.detailed_description,
        'features': project.feature_list,
        'technologies': project.tech_list,
        'image_url': project.image.url if project.image else project.image_url,
        'github_url': project.github_url,
        'live_demo_url': project.live_demo_url,
        'created_at': project.created_at.strftime('%B %Y')
    }
    return JsonResponse(data)
