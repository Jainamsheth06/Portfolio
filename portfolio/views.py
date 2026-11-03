from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import threading
import logging
import sys
from .models import Profile, SkillCategory, Skill, Education, ProjectCategory, Project, ContactMessage
from .forms import ContactForm

logger = logging.getLogger(__name__)

def get_default_profile():
    return {
        'full_name': 'Jainam Sheth',
        'title': 'Full Stack Developer & Software Engineer',
        'subtitle_roles': 'Full Stack Developer, Django Specialist, Python Engineer',
        'bio': 'I architect robust backends, design intuitive frontends, and create seamless web experiences using Django, modern JavaScript, and clean coding standards.',
        'about_text': "I am a dedicated software developer specializing in Python, Django, modern JavaScript, and responsive web design. I enjoy turning complex system designs into clean, maintainable, and user-centric web applications. Whether crafting RESTful APIs, optimizing relational databases, or styling pixel-perfect user interfaces, I bring technical precision and artistic care to every project.",
        'avatar_url': '/static/images/profile.png',
        'email': 'jainamsheth2006@gmail.com',
        'phone': '+91 9924377710',
        'phone_clean': '+919924377710',
        'whatsapp_number': '919924377710',
        'location': 'Ahmedabad',
        'github_url': 'https://github.com/Jainamsheth06',
        'linkedin_url': 'https://www.linkedin.com/in/jainam--sheth',
        'instagram_url': 'https://www.instagram.com/mr_jainamsheth',
        'twitter_url': 'https://x.com/jainam216sheth',
        'completed_projects': 5,
        'happy_clients': 5,
        'satisfaction_rate': 100,
        'available_for_hire': True,
    }

def send_async_email(subject, message, from_email, recipient_list):
    """Sends email in background thread without blocking the user response."""
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
    except Exception as e:
        logger.error(f"Error delivering email via SMTP: {e}")

def index(request):
    profile = Profile.objects.filter(is_active=True).first()
    if not profile:
        profile = get_default_profile()

    categories = SkillCategory.objects.prefetch_related('skills').all()
    educations = Education.objects.all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.select_related('category').all()
    contact_form = ContactForm()

    context = {
        'profile': profile,
        'skill_categories': categories,
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

            # Prepare email notification
            recipient = getattr(settings, 'RECIPIENT_EMAIL', settings.EMAIL_HOST_USER)
            email_subject = f"[Portfolio Contact] {contact.subject} - {contact.name}"
            email_body = (
                f"Hello Jainam,\n\n"
                f"You have received a new contact inquiry from your portfolio website!\n\n"
                f"--------------------------------------------------\n"
                f"Sender Name : {contact.name}\n"
                f"Sender Email: {contact.email}\n"
                f"Subject     : {contact.subject}\n"
                f"--------------------------------------------------\n\n"
                f"Message:\n{contact.message}\n\n"
                f"--------------------------------------------------\n"
                f"Reply directly to: {contact.email}\n"
            )

            # Fire email in background daemon thread for instant user feedback
            email_thread = threading.Thread(
                target=send_async_email,
                args=(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, [recipient]),
                daemon=True
            )
            email_thread.start()
            if 'test' in sys.argv:
                email_thread.join(timeout=2.0)

            msg = f"Thank you, {contact.name}! Your message has been sent directly to my email. I will get back to you shortly."
            if is_ajax:
                return JsonResponse({'status': 'success', 'message': msg})
            messages.success(request, msg)
            return redirect('/#contact')
        else:
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
