#!/usr/bin/env python3
"""Simple script to seed demo data for local development.

Usage: from project root run `python scripts/seed_demo_data.py`
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_project.settings')
django.setup()

from apps.crm_core.models import Account, Lead, Deal, Task
from apps.accounts.models import Contact


def run():
    print('Seeding demo data...')
    Account.objects.all().delete()
    Contact.objects.all().delete()
    Lead.objects.all().delete()
    Deal.objects.all().delete()
    Task.objects.all().delete()

    acc1 = Account.objects.create(name='Acme Corp', industry='Manufacturing')
    acc2 = Account.objects.create(name='Beta LLC', industry='Software')

    Contact.objects.create(first_name='Alice', last_name='Anderson', email='alice@acme.local')
    Contact.objects.create(first_name='Bob', last_name='Brown', email='bob@beta.local')

    Lead.objects.create(account=acc1, name='Charlie Lead', email='charlie@lead.local', status='new')
    Deal.objects.create(account=acc2, title='Platform License', value=4999.99, stage='proposal')
    Task.objects.create(account=acc1, subject='Follow up call', completed=False)

    print('Done.')


if __name__ == '__main__':
    run()
