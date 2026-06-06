#!/usr/bin/env python3
"""Seed demo leads for MVP verification."""
import os
import django
import sys

if __name__ == '__main__':
    # Ensure project root is on PYTHONPATH so Django settings import works
    project_root = os.path.dirname(os.path.dirname(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_project.settings')
    django.setup()

    from apps.crm_core.models import Lead

    samples = [
        {'name': 'Alpha Corp', 'email': 'alpha@example.com', 'status': 'new'},
        {'name': 'Beta LLC', 'email': 'beta@example.com', 'status': 'contacted'},
        {'name': 'Gamma Co', 'email': 'gamma@example.com', 'status': 'qualified'},
    ]

    for s in samples:
        lead, created = Lead.objects.get_or_create(name=s['name'], defaults={
            'email': s['email'], 'status': s['status']
        })
        if created:
            print('Created lead', lead.name)
        else:
            print('Exists', lead.name)
