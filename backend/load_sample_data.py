"""
Load sample data for ShieldHer platform testing
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.lessons.models import Lesson
from apps.resources.models import Resource, Helpline

# Create sample lessons
lessons_data = [
    {
        'title': 'Understanding Digital Privacy',
        'description': 'Learn the basics of protecting your personal information online',
        'category': 'privacy',
        'difficulty': 'beginner',
        'duration_minutes': 15,
        'content': {'sections': [{'title': 'Introduction', 'text': 'Digital privacy is about controlling who has access to your personal information...'}]},
        'published': True,
    },
    {
        'title': 'Recognizing Online Harassment',
        'description': 'Identify different forms of digital violence and harassment',
        'category': 'awareness',
        'difficulty': 'beginner',
        'duration_minutes': 20,
        'content': {'sections': [{'title': 'Introduction', 'text': 'Online harassment can take many forms including cyberbullying, stalking, and threats...'}]},
        'published': True,
    },
    {
        'title': 'Securing Your Social Media',
        'description': 'Best practices for privacy settings on social platforms',
        'category': 'security',
        'difficulty': 'intermediate',
        'duration_minutes': 25,
        'content': {'sections': [{'title': 'Introduction', 'text': 'Social media platforms collect vast amounts of data. Learn how to protect yourself...'}]},
        'published': True,
    },
]

print("Creating sample lessons...")
for lesson_data in lessons_data:
    lesson, created = Lesson.objects.get_or_create(
        title=lesson_data['title'],
        defaults=lesson_data
    )
    if created:
        print(f"✓ Created lesson: {lesson.title}")
    else:
        print(f"- Lesson already exists: {lesson.title}")

# Create sample resources
resources_data = [
    {
        'title': 'National Domestic Violence Hotline',
        'description': 'Free, confidential support 24/7 for victims of domestic violence. Call 1-800-799-7233',
        'content': 'The National Domestic Violence Hotline provides 24/7 support for victims of domestic violence. All calls are confidential and anonymous.',
        'category': 'organizations',
        'resource_type': 'organization',
        'external_url': 'https://www.thehotline.org',
        'is_published': True,
    },
    {
        'title': 'Cyber Civil Rights Initiative',
        'description': 'Support for victims of non-consensual pornography and online abuse',
        'content': 'The Cyber Civil Rights Initiative provides support, resources, and advocacy for victims of non-consensual pornography and online abuse.',
        'category': 'organizations',
        'resource_type': 'organization',
        'external_url': 'https://www.cybercivilrights.org',
        'is_published': True,
    },
    {
        'title': 'RAINN - National Sexual Assault Hotline',
        'description': 'National sexual assault hotline and online chat. Call 1-800-656-4673',
        'content': 'RAINN (Rape, Abuse & Incest National Network) operates the National Sexual Assault Hotline. Available 24/7 with free, confidential support.',
        'category': 'organizations',
        'resource_type': 'organization',
        'external_url': 'https://www.rainn.org',
        'is_published': True,
    },
]

print("\nCreating sample resources...")
for resource_data in resources_data:
    resource, created = Resource.objects.get_or_create(
        title=resource_data['title'],
        defaults=resource_data
    )
    if created:
        print(f"✓ Created resource: {resource.title}")
    else:
        print(f"- Resource already exists: {resource.title}")

# Create sample helplines
helplines_data = [
    {
        'name': 'Crisis Text Line',
        'phone_number': 'Text HOME to 741741',
        'description': 'Free 24/7 crisis support via text message',
        'category': 'crisis',
        'availability': '24/7',
        'is_24_7': True,
        'languages': ['English', 'Spanish'],
    },
    {
        'name': 'National Suicide Prevention Lifeline',
        'phone_number': '988',
        'description': 'Free and confidential support for people in distress',
        'category': 'crisis',
        'availability': '24/7',
        'is_24_7': True,
        'languages': ['English', 'Spanish'],
    },
]

print("\nCreating sample helplines...")
for helpline_data in helplines_data:
    helpline, created = Helpline.objects.get_or_create(
        name=helpline_data['name'],
        defaults=helpline_data
    )
    if created:
        print(f"✓ Created helpline: {helpline.name}")
    else:
        print(f"- Helpline already exists: {helpline.name}")

print("\n✅ Sample data loaded successfully!")
print("\nYou can now:")
print("- View lessons at: http://localhost:3000/lessons")
print("- View resources at: http://localhost:3000/resources")
print("- Submit anonymous reports at: http://localhost:3000/report")
print("- Access admin panel at: http://127.0.0.1:8000/admin/")
print("  Username: admin@shieldher.com")
print("  Password: admin123")
