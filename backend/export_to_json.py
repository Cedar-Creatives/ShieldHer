"""
Export lessons, helplines, and resources to static JSON files.
"""

import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.lessons.models import Lesson
from apps.resources.models import Helpline, Resource


def export_lessons():
    """Export lessons to JSON"""
    lessons = []
    for lesson in Lesson.objects.filter(published=True).order_by('id'):
        lessons.append({
            'id': lesson.id,
            'title': lesson.title,
            'description': lesson.description,
            'category': lesson.category,
            'difficulty': lesson.difficulty,
            'duration_minutes': lesson.duration_minutes,
            'content': lesson.content,
            'quiz': lesson.quiz,
            'thumbnail_url': lesson.thumbnail_url,
            'created_at': lesson.created_at.isoformat(),
        })
    
    output_path = '../frontend/src/data/lessons.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Exported {len(lessons)} lessons to {output_path}")
    return lessons


def export_helplines():
    """Export helplines to JSON"""
    helplines = []
    for helpline in Helpline.objects.filter(is_active=True).order_by('-priority', 'name'):
        helplines.append({
            'id': helpline.id,
            'name': helpline.name,
            'phone_number': helpline.phone_number,
            'description': helpline.description,
            'category': helpline.category,
            'availability': helpline.availability,
            'is_24_7': helpline.is_24_7,
            'languages': helpline.languages,
        })
    
    output_path = '../frontend/src/data/helplines.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(helplines, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Exported {len(helplines)} helplines to {output_path}")
    return helplines


def export_resources():
    """Export resources to JSON"""
    resources = []
    for resource in Resource.objects.filter(is_published=True).order_by('-created_at'):
        resources.append({
            'id': resource.id,
            'title': resource.title,
            'description': resource.description,
            'content': resource.content,
            'category': resource.category,
            'resource_type': resource.resource_type,
            'external_url': resource.external_url,
            'tags': resource.tags,
            'created_at': resource.created_at.isoformat(),
        })
    
    output_path = '../frontend/src/data/resources.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(resources, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Exported {len(resources)} resources to {output_path}")
    return resources


if __name__ == '__main__':
    print("Exporting data to static JSON files...\n")
    
    lessons = export_lessons()
    helplines = export_helplines()
    resources = export_resources()
    
    print(f"\n✅ Export complete!")
    print(f"   - {len(lessons)} lessons")
    print(f"   - {len(helplines)} helplines")
    print(f"   - {len(resources)} resources")
