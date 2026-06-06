from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    """Create default RBAC groups and assign sensible permissions."""
    if sender.name != 'apps.accounts' and sender.name != 'apps.crm_core':
        # Run only once when accounts or crm_core migrations run
        return

    # Define group -> model permissions mapping
    roles = {
        'Admin': {
            'all_models': True,
        },
        'Sales': {
            'models': ['account', 'lead', 'deal', 'contact'],
            'perms': ['add', 'change', 'view'],
        },
        'Support': {
            'models': ['contact', 'task'],
            'perms': ['add', 'change', 'view'],
        },
    }

    # Helper to get permissions for a model
    def get_model_perms(model_name, perms):
        out = []
        try:
            ct = ContentType.objects.get(model=model_name)
        except ContentType.DoesNotExist:
            return out
        for p in perms:
            codename = f"{p}_{model_name}"
            try:
                perm = Permission.objects.get(codename=codename, content_type=ct)
                out.append(perm)
            except Permission.DoesNotExist:
                continue
        return out

    # Create or update groups
    for role_name, cfg in roles.items():
        group, _ = Group.objects.get_or_create(name=role_name)
        # clear current perms and reassign
        group.permissions.clear()
        if cfg.get('all_models'):
            # assign all permissions
            perms = Permission.objects.all()
            group.permissions.set(perms)
            continue

        models = cfg.get('models', [])
        perms = cfg.get('perms', ['view'])
        for m in models:
            model_perms = get_model_perms(m, perms)
            for p in model_perms:
                group.permissions.add(p)
