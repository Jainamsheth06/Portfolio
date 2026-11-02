from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Profile, SkillCategory, Skill, Experience, Education, ProjectCategory, Project, ContactMessage

class PortfolioTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            full_name="Alex Morgan",
            title="Full Stack Software Engineer",
            email="alex@example.com"
        )
        self.cat = ProjectCategory.objects.create(name="Full Stack", slug="full-stack")
        self.project = Project.objects.create(
            category=self.cat,
            title="Test Project",
            slug="test-project",
            short_description="Short desc",
            detailed_description="Long detailed description",
            key_features="Feature 1\nFeature 2",
            technologies="Django, Python, JavaScript"
        )

    def test_index_view_status_and_content(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alex Morgan")
        self.assertContains(response, "Test Project")
        self.assertTemplateUsed(response, 'portfolio/index.html')

    def test_contact_submit_ajax_success(self):
        data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'subject': 'Project Inquiry',
            'message': 'Hello, I would like to discuss a project with you.'
        }
        response = self.client.post(
            reverse('portfolio:contact_submit'),
            data=data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data['status'], 'success')
        self.assertTrue(ContactMessage.objects.filter(email='jane@example.com').exists())

    def test_contact_submit_ajax_invalid(self):
        # Missing required email and message
        data = {
            'name': 'Jane Doe',
            'subject': 'Inquiry'
        }
        response = self.client.post(
            reverse('portfolio:contact_submit'),
            data=data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 400)
        json_data = response.json()
        self.assertEqual(json_data['status'], 'error')
        self.assertIn('email', json_data['errors'])

    def test_project_detail_api(self):
        response = self.client.get(reverse('portfolio:project_detail_api', kwargs={'slug': self.project.slug}))
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data['title'], "Test Project")
        self.assertEqual(json_data['category'], "Full Stack")
        self.assertIn("Django", json_data['technologies'])
        self.assertEqual(len(json_data['features']), 2)
